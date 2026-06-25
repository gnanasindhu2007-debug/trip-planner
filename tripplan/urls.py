from django.urls import path
from .views import tripplan

urlpatterns = [
    path('', tripplan, name='tripplan'),
]