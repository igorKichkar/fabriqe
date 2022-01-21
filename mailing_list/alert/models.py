from django.db import models


class Mailing(models.Model):
    mailing_start = models.DateTimeField()
    message = models.TextField()
    filter_client = models.CharField(max_length=100)
    mailing_end = models.DateTimeField()


class Customer(models.Model):
    phone = models.CharField(max_length=11)
    code_phone = models.CharField(max_length=10)
    tag = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=50)


class Massage(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, null=True)