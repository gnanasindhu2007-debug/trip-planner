from django.urls import path
from .views import itinerary

urlpatterns = [
    path('', itinerary, name='itinerary'),
]