# routing goes here
from django.urls import path
from . import views

urlpatterns = [
    path('', views.placeholder, name='adminpanel_home'),
]