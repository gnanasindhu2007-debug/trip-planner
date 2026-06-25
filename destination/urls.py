from django.urls import path
from .views import destination

urlpatterns = [
    path('', destination, name='destination'),
]