from django.urls import path
from .views import HomeResponse

urlpatterns = [
    path('', HomeResponse.as_view())
]
