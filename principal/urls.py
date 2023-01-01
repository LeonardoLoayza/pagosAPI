from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from users.views import UserCreateView, UserListView
from pago.views import Rest_Services, Rest_Payments, Rest_Payments_expired
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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

router = routers.DefaultRouter()
router.register(r'services', Rest_Services, 'Services')
router.register(r'payments', Rest_Payments, 'Payments')
router.register(r'payments-expired', Rest_Payments_expired, 'Payments-expired')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('users/all/', UserListView.as_view(), name='user-list'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(),  name="refresh_token"),
]

urlpatterns += router.urls

