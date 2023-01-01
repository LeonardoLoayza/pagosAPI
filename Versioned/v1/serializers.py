# from rest_framework import serializers
# from pago.models import Services
# from pago.models import Payments, Payments_expired

# class ServicesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Services
#         fields = '__all__'
        
# class PaymentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payments
#         fields = '__all__'

#     def validate(self,data):
#         amount = data.get('amount')
#         if amount < 0:
#             raise serializers.ValidationError('Amount can\'t be negative')
#         return data

# class Payments_expiredSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payments_expired
#         fields = '__all__'


    


        