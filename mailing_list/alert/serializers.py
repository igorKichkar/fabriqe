from rest_framework import serializers
from .models import Mailing, Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ['id']


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        exclude = ['id']
