# routing for worker app goes here
from django.urls import path
from . import views

app_name = "worker"

urlpatterns = [

    path('dashboard/', views.worker_dashboard, name='worker_dashboard'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    
    path('available-jobs/', views.available_jobs, name='available_jobs'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    path('assigned-jobs/', views.assigned_jobs, name='assigned_jobs'),
    path('profile/', views.profile, name='profile'),

]