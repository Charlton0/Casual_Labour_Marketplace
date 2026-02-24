# routing for client app goes here
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]