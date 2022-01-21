from django.urls import path
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('', first_view, name='first_view'),
 
]

