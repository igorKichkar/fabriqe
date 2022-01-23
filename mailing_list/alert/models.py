from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator


class Mailing(models.Model):
    mailing_start = models.DateTimeField()
    mailing_end = models.DateTimeField()
    message_text = models.TextField()
    filter_client = models.JSONField(null=True)


class Client(models.Model):
    phone_number = RegexValidator(
        regex=r'^\d{9,15}$',
        message="Phone number. Up to 15 digits allowed."
    )
    phone = models.CharField(
        validators=[phone_number], max_length=17, blank=True)

    code = RegexValidator(
        regex=r'^\d{3,5}$',
        message="Phone code. Up to 5 digits allowed."
    )
    code_phone = models.CharField(validators=[code], max_length=5, blank=True)
    tag = models.CharField(max_length=100)
    time_zone = models.IntegerField(
        default=3, validators=[MinValueValidator(-12), MaxValueValidator(14)])


class Message(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, null=True)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True)
    mailing = models.ForeignKey(
        Mailing, on_delete=models.SET_NULL, null=True, related_name='sent_mailings')
