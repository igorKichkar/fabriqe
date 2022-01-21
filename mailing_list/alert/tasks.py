from mailing_list.celery import app
from django.contrib.auth.models import User
import requests




@app.task
def ok():
    print('work!!!!!')

name = 0
@app.task
def ok_2():
    r = requests.get('http://127.0.0.1:8000')
    print(r.content)
    print('work!!!!! OK_2')

