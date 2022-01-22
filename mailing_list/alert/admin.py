from django.contrib import admin
from .models import Mailing, Customer, Message


admin.site.register(Mailing)
admin.site.register(Customer)
admin.site.register(Message)
