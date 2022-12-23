from django.contrib import admin
from .models import Service, PaymentUser, ExpiredPayment

# Register your models here.

admin.site.register(Service)
admin.site.register(PaymentUser)
admin.site.register(ExpiredPayment)