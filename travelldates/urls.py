from django.urls import path
from .views import travelldates

urlpatterns = [
    path('', travelldates, name='travelldates'),
]