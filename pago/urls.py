from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ServiceListCreate, ServiceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('services/', ServiceListCreate.as_view(), name='service'),
    path("servicesTweak/", ServiceRetrieveUpdateDestroyAPIView.as_view(), name="service")
]
