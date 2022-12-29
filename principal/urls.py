from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from pago.urls import urlpatterns as pago_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# import versioned todo?

schema_view = get_schema_view (
    openapi.Info(
        title="PagosAPI",
        default_version="v1",
        description="API de pagos",
        terms_of_service="httsp://www.google.com/policies/terms/",
        contact=openapi.Contact(email="LeonardoLoayza28@gmail.com"),
        license=openapi.License(name="BSD License"),        
    ),
    public=True,
    permission_classes=[AllowAny]    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path(r'payments/', include('pago.urls')),
    
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    
]

