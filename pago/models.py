from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField() # no obligatorio
    logo = models.URLField(max_length=255)
    prefix = models.CharField(max_length=3, default='NNN')

    def __str__(self) -> str:
        return self.name

class Payments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    expiration_date = models.DateField()

class Payments_expired(models.Model):
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)
    amount_fee = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
