from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Mailing, Customer, Message
from .serializers import CustomerSerializer, MailingSerializer, MailingStatisticsDetatilSerializer


class CustomerView(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class MailingView(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MailingStatisticsDetatilView(RetrieveModelMixin, GenericViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingStatisticsDetatilSerializer


class MailingGeneralStatisticsView(APIView):

    def get(self, request, format=None):
        mailings = Mailing.objects.all().count()
        ok_200 = Message.objects.filter(status='200').count()
        bad_pequest_400 = Message.objects.filter(status='400').count()
        data = {'mailings': mailings,
                'ok_200': ok_200,
                'bad_pequest_400': bad_pequest_400}
        return Response(data)
