from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from client.models import Job
from .models import JobApplication


@login_required
def worker_dashboard(request):

    # Get all available jobs (not just count)
    available_jobs = Job.objects.filter(status="Available")

    # Counts for dashboard cards
    available_jobs_count = available_jobs.count()
    applied_jobs_count = JobApplication.objects.filter(worker=request.user).count()
    assigned_jobs_count = Job.objects.filter(assigned_worker=request.user).count()

    # Recent jobs (for table display)
    recent_jobs = available_jobs[:5]

    # Jobs already applied for (to disable Apply button)
    applied_job_ids = JobApplication.objects.filter(
        worker=request.user
    ).values_list('job_id', flat=True)

    context = {
        "available_jobs_count": available_jobs_count,
        "applied_jobs": applied_jobs_count,
        "assigned_jobs": assigned_jobs_count,
        "recent_jobs": recent_jobs,
        "applied_job_ids": applied_job_ids,
    }

    return render(request, "worker/dashboard.html", context)


# ================================
# APPLY FOR JOB
# ================================
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    # Prevent duplicate applications
    already_applied = JobApplication.objects.filter(
        job=job,
        worker=request.user
    ).exists()

    if not already_applied:
        JobApplication.objects.create(
            job=job,
            worker=request.user,
            status="Pending"
        )

    return redirect('worker:worker_dashboard')


# ================================
# AVAILABLE JOBS PAGE
# ================================
@login_required
def available_jobs(request):

    jobs = Job.objects.filter(status="Available")

    applied_job_ids = JobApplication.objects.filter(
        worker=request.user
    ).values_list('job_id', flat=True)

    context = {
        "jobs": jobs,
        "applied_job_ids": applied_job_ids,
    }

    return render(request, "worker/available_jobs.html", context)


# ================================
# APPLIED JOBS PAGE
# ================================
@login_required
def applied_jobs(request):

    applications = JobApplication.objects.filter(worker=request.user)

    return render(request, "worker/applied_jobs.html", {
        "applications": applications
    })


# ================================
# ASSIGNED JOBS PAGE
# ================================
@login_required
def assigned_jobs(request):

    jobs = Job.objects.filter(assigned_worker=request.user)

    return render(request, "worker/assigned_jobs.html", {
        "jobs": jobs
    })


# ================================
# PROFILE PAGE
# ================================
@login_required
def profile(request):
    return render(request, "worker/profile.html")