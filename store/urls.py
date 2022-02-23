from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Faizan Store",
      default_version='v1',
      description="Store Information",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('productinfo/', views.getproduct1.as_view()),
    path('productinfo/<int:pk>', views.getproduct.as_view()),
    path('productinfo/post/', views.postproduct.as_view()),
    path('productinfo/put/', views.putproduct.as_view()),
    path('productinfo/delete/', views.deleteproduct.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('gettoken/', TokenObtainPairView.as_view(), name = 'gettoken'),
	path('refreshtoken/', TokenRefreshView.as_view(), name = 'refreshtoken'),

]