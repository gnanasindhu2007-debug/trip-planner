from django.urls import path
from .views import googlemaps

urlpatterns = [
    path('', googlemaps, name='googlemaps'),
]