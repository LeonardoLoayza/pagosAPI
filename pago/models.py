from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    class Service(models.TextChoices):
        YOUTUBE = 'YT', _('Youtube')
        SPOTIFY = 'SP', _('Spotify')
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')
    
    name = models.CharField(max_length=2, choices=Service.choices, default=Service.YOUTUBE,)
    description = models.CharField(max_length=300)
    logo = models.CharField(max_length=100)
    
    def __str__(self) -> str: 
        return self.name

class PaymentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    payment_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    expiration_date = models.DateTimeField(auto_now_add=False)

    def __str__(self) -> str:
        return self.service_id

class ExpiredPayment(models.Model):
    payment_user_id = models.ForeignKey(PaymentUser, on_delete=models.CASCADE)
    penalty_fee_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    def __str__(self) -> str:
        return self.payment_user_id