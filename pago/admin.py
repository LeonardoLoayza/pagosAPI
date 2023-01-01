from django.contrib import admin
from .models import Services, Payments, Payments_expired

# Register your models here.

admin.site.register(Services)
admin.site.register(Payments)
admin.site.register(Payments_expired)