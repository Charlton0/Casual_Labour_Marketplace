# routing goes here
from django.urls import path, reverse_lazy
from .views import (
    register_role,
    register_client,
    register_worker,
    login_view,
    logout_view,
)

from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [

    # =============================
    # AUTHENTICATION
    # =============================

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # =============================
    # REGISTRATION FLOW
    # =============================

    # Specific routes first
    path('register/client/', register_client, name='register_client'),
    path('register/worker/', register_worker, name='register_worker'),

    # General route last
    path('register/', register_role, name='register_role'),

    # =============================
    # PASSWORD RESET FLOW
    # =============================

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt',
            success_url=reverse_lazy('accounts:password_reset_done')
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'  # ✅ fixed
        ),
        name='password_reset_complete'
    ),
]