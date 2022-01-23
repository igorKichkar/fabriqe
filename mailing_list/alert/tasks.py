from datetime import datetime, time
import requests
import json

from django.utils.timezone import make_naive

from .models import Mailing, Client, Message
from mailing_list.celery import app
from django.core.mail import send_mail


def send_message(data, mailing_end):
    json_data = json.dumps(data)
    while True:
        r = requests.post(
            'https://probe.fbrq.cloud/v1/send/' + str(data['id']),
            headers={
                'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzQyOTI3MTQsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Iklnb3IuS2ljaGthciJ9.oZRYq4zhgfq3Vnfn-6jjMRLpQVmS7k-0V7AlFrZouBc'},
            data=json_data
        )

        if r.status_code != 200:
            if mailing_end > datetime.now():
                time.sleep(10)
                continue
            return None

        return r.status_code


@app.task
def sending():
    for mailing in Mailing.objects.filter(mailing_start__lt=datetime.now(), mailing_end__gt=datetime.now()):
        mailing_start = make_naive(mailing.mailing_start)
        mailing_end = make_naive(mailing.mailing_end)
        for client in Client.objects.filter(code_phone=mailing.filter_client[1]['code_phone'], tag=mailing.filter_client[0]['tag']):

            if mailing_start < datetime.now() < mailing_end:
                message = Message.objects.create(
                    client=client, mailing=mailing)
                data = {
                    "id": message.id,
                    "phone": client.phone,
                    "text": mailing.message_text
                }

                message.status = send_message(data, mailing_end)
                message.save()
            else:
                Message.objects.create(
                    client=client, mailing=mailing, status=None)


@app.task
# enter your email and password in settings.py
def send_daily_statistics():
    mailings = Mailing.objects.all().count()
    ok_200 = Message.objects.filter(status='200').count()
    bad_pequest_400 = Message.objects.filter(status='400').count()
    message = f'''
    date: {datetime.now().ctime()}
    mailings: {mailings},
    ok_200: {ok_200},
    bad_pequest_400: {bad_pequest_400}'''
    send_mail(
        'Daily statistics.',
        message,
        'igorkich947@gmail.com',
        ['igor_kichkar@mail.ru'],
        fail_silently=False,
    )
