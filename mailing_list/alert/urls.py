from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from .views import CustomerView, MailingView

router = routers.DefaultRouter()
router.register(r'clients', CustomerView)
router.register(r'mailings', MailingView)

urlpatterns = [
    path('', include(router.urls)),
    path('openapi/', get_schema_view(
        title="Fabriqe",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
