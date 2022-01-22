from django.urls import include, path
from rest_framework import routers
from .views import CustomerView, MailingView, MailingStatisticsDetatilView, MailingGeneralStatisticsView

router = routers.DefaultRouter()
router.register(r'customers', CustomerView)
router.register(r'mailings', MailingView)
router.register(r'mailing-statistics-detatil', MailingStatisticsDetatilView)

urlpatterns = [
    path('', include(router.urls)),
    path('mailing-general-statistics/', MailingGeneralStatisticsView.as_view() )
]