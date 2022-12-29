from rest_framework import serializers
from pago.models import Service, PaymentUser, ExpiredPayment
from django.utils import timezone 

class ServiceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length = 100)
    description = serializers.CharField(max_length = 300)
    logo = serializers.CharField(max_length = 100)
    
    class Meta: 
        model = Service 
        fields = '__all__'

class PaymentUserSerializer(serializers.ModelSerializer):
    service_id = serializers.IntegerField()
    
    class Meta: 
        model = PaymentUser
        fields = '__all__'
        
    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor a 0")
        if value > 10000:
            raise serializers.ValidationError("El monto debe ser mayor a 10000")
        return value

    def validate_payment_date(self, value):

        if value <= timezone.now():
            raise serializers.ValidationError("Fecha invalida")
        return value

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ExpiredPayment 
        fields = '__all__'
     
    def validate_penalty_fee_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Valor mayor que 0")
        return value  

        

        