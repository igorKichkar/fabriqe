import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_list.settings')

app = Celery('mailing_list')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending': {
        'task': 'alert.tasks.sending',
        'schedule': crontab(minute='*/1'),
    },
    'send_daily_statistics': {
        'task': 'alert.tasks.send_daily_statistics',
        'schedule': crontab(minute=0, hour='*/24'),
    },
}
