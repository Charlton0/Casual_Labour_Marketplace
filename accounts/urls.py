# routing goes here
from django.urls import path
from .views import (
    register_role,
    register_client,
    register_worker,
    login_view,
    password_reset_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),

    # Specific URLs first
    path('register/client/', register_client, name='register_client'),
    path('register/worker/', register_worker, name='register_worker'),

    # General URL last
    path('register/', register_role, name='register_role'),

    path('password-reset/', password_reset_view, name='password_reset'),
]

