from django.shortcuts import render
from rest_framework import viewsets
from .models import Payments, Payments_expired, Services
from .serializers import PaymentsSerializer, Payments_expiredSerializer, ServicesSerializer
from rest_framework.response import Response
from rest_framework import status
from .pagination import PaginationPagos
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class Rest_Payments(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    pagination_class = PaginationPagos

    throttle_scope = 'pago'

    def create(self, request):        
        serializer = PaymentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            payment_date = serializer.data.get('payment_date')
            expiration_date = serializer.data.get('expiration_date')
            if expiration_date<payment_date:
                record = {
                    "amount_fee": 0.2*float(serializer.data.get('amount')),
                    "payment_id":serializer.data.get('id'),
                    "amount": serializer.data.get('amount'),
                    "service_id": serializer.data.get('service_id'),
                    "user_id": serializer.data.get('user_id'),
                }

                serializer2 = Payments_expiredSerializer(data=record)
                if serializer2.is_valid():
                    serializer2.save()
                    return Response({
                        "ok":True,
                        "message":"Record added",
                        "data 1":serializer.data,
                        "message":"Record added also in Expired Payments",
                        "data 2":serializer2.data
                }, status=status.HTTP_201_CREATED)

            return Response({
                "ok":True,
                "message":"Record created",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Rest_Payments_expired(viewsets.ModelViewSet):
    queryset = Payments_expired.objects.all()
    serializer_class = Payments_expiredSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return [AllowAny()]
    

class Rest_Services(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
