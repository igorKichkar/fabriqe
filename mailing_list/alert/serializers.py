from rest_framework import serializers
from .models import Mailing, Customer, Message


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['phone', 'code_phone', 'tag', 'time_zone']


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = ['mailing_start', 'message', 'filter_client', 'mailing_end']


class MailingStatisticsDetatilSerializer(serializers.ModelSerializer):
    ok_200 = serializers.SerializerMethodField()
    bad_pequest_400 = serializers.SerializerMethodField()

    def get_ok_200(self, instance):
        return Message.objects.filter(mailing=instance, status='200').count()

    def get_bad_pequest_400(self, instance):
        return Message.objects.filter(mailing=instance, status='400').count()

    class Meta:
        model = Mailing
        fields = ['id', 'ok_200', 'bad_pequest_400']
