import datetime
from django.utils import timezone
from django.test import TestCase
from alert.serializers import CustomerSerializer, MailingSerializer, MailingStatisticsDetatilSerializer
from alert.models import Mailing, Customer, Message


class CustomerSerializerTestCase(TestCase):
    def test_ok(self):
        Customer.objects.create(
            phone='70123456789', code_phone='375', tag='some_tag', time_zone='Europe/Minsk')
        Customer.objects.create(
            phone='71123456789', code_phone='375', tag='some_tag_2', time_zone='Europe/Minsk')
        customers = Customer.objects.all()
        data = CustomerSerializer(customers, many=True).data
        expected_data = [
            {
                'phone': '70123456789',
                'code_phone': '375',
                'tag': 'some_tag',
                'time_zone': 'Europe/Minsk'
            },
            {
                'phone': '71123456789',
                'code_phone': '375',
                'tag': 'some_tag_2',
                'time_zone': 'Europe/Minsk'
            }
        ]
        self.assertEqual(expected_data, data)


class MailingSerializerTestCase(TestCase):
    def test_ok(self):
        mailing_1 = Mailing.objects.create(
            mailing_start=timezone.now(), message='message', filter_client='some_tag',
            mailing_end=timezone.now() + datetime.timedelta(days=30)
        )
        mailing_2 = Mailing.objects.create(
            mailing_start=timezone.now(), message='message_2', filter_client='375',
            mailing_end=timezone.now() + datetime.timedelta(days=30)
        )
        malings = Mailing.objects.all()
        data = MailingSerializer(malings, many=True).data
        expected_data = [
            {
                'mailing_start': mailing_1.mailing_start.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'message': mailing_1.message,
                'filter_client': mailing_1.filter_client,
                'mailing_end': mailing_1.mailing_end.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            },
            {
                'mailing_start': mailing_2.mailing_start.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'message': mailing_2.message,
                'filter_client': mailing_2.filter_client,
                'mailing_end': mailing_2.mailing_end.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        ]
        self.assertEqual(expected_data, data)


class MailingStatisticsDetatilSerializerTestCase(TestCase):
    def test_ok(self):
        mailing = Mailing.objects.create(
            mailing_start=timezone.now(), message='message', filter_client='some_tag',
            mailing_end=timezone.now() + datetime.timedelta(days=30)
        )
        customer_1 = Customer.objects.create(
            phone='70123456789', code_phone='375', tag='some_tag', time_zone='Europe/Minsk'
        )
        Message.objects.create(
            status='200', customer=customer_1, mailing=mailing
        )
        malings = Mailing.objects.all()
        data = MailingStatisticsDetatilSerializer(malings, many=True).data
        expected_data = [
            {
                'id': mailing.id,
                'ok_200': 1,
                'bad_pequest_400': 0,
            }
        ]
        self.assertEqual(expected_data, data)
