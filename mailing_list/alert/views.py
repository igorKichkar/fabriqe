from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Mailing, Client, Message
from .serializers import ClientSerializer, MailingSerializer


class CustomerView(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingView(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    @action(detail=True, methods=['GET'])
    def detail_statistics(self, request,  pk: int):
        mailing = self.get_object()
        data = {'id mailing': mailing.id,
                'ok_200': mailing.sent_mailings.filter(status='200').count(),
                'bad_pequest_400': mailing.sent_mailings.filter(status='400').count()
                }
        return Response(data)

    @action(detail=False, methods=['GET'])
    def general_statistics(self, request):
        mailings = Mailing.objects.all().count()
        ok_200 = Message.objects.filter(status='200').count()
        bad_pequest_400 = Message.objects.filter(status='400').count()
        data = {'mailings': mailings,
                'ok_200': ok_200,
                'bad_pequest_400': bad_pequest_400}
        return Response(data)
