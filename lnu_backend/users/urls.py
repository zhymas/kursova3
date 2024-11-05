from django.urls import path
from .views import HomeResponse, Claims
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', HomeResponse.as_view(), name='index'),
    path('claims/', Claims.as_view())
]
