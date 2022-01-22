from datetime import datetime
import requests
import json

from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.timezone import make_naive

from .models import Mailing, Customer, Message
from mailing_list.celery import app


@app.task
def ok():
    print('work!!!!!')


@app.task
def sending():
    criterion1 = Q(mailing_start__lt=datetime.now())
    criterion2 = Q(mailing_end__gt=datetime.now())
    mailings = Mailing.objects.filter(criterion1 & criterion2)

    for i in mailings:
        mailing_start = make_naive(i.mailing_start)
        mailing_end = make_naive(i.mailing_end)
        
        if mailing_start < datetime.now() and mailing_end > datetime.now():
            mailing_start = make_naive(i.mailing_start)
            criterion1 = Q(code_phone=i.filter_client)
            criterion2 = Q(tag=i.filter_client)
            customers = Customer.objects.filter(criterion1 | criterion2)

            for j in customers:
                massage = Message.objects.create(customer=j, mailing=i)
                data = {
                    "id": massage.id,
                    "phone": j.phone,
                    "text": i.message
                }
                json_data = json.dumps(data)
                r = requests.post(
                    'https://probe.fbrq.cloud/v1/send/' + str(massage.id),
                    headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzQyOTI3MTQsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Iklnb3IuS2ljaGthciJ9.oZRYq4zhgfq3Vnfn-6jjMRLpQVmS7k-0V7AlFrZouBc'},
                    data=json_data
                )
                massage.status = r.status_code
                massage.save()
