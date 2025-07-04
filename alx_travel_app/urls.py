# alxtravelapp/urls.py

from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Setup for drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="AlxTravelApp API",
      default_version='v1',
      description="API documentation for the AlxTravelApp project. This API provides endpoints for managing travel listings and related functionalities.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@alxtravelapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]