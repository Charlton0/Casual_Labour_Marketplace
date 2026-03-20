from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.client_dashboard, name='dashboard'),
    path('post-job/', views.post_job, name='post_job'),
    path('jobs/', views.client_jobs, name='jobs'),
    path('complete-job/<int:job_id>/', views.complete_job, name='complete_job'),

]