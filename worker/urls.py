# routing for worker app goes here
from django.urls import path
from . import views

urlpatterns = [
    path('', views.placeholder, name='worker_home'),
]