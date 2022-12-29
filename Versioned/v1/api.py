from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from pago.models import Service 
from .pagination import PaginationPagos
from .serializers import ServiceSerializer

class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationPagos
    
class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer 
    
    permission_classes = [IsAdminUser, TokenAuthentication]
    lookup_field = 'id'
    


    



