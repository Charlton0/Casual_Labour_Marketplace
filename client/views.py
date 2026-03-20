from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job


# CLIENT DASHBOARD
@login_required
def client_dashboard(request):

    jobs = Job.objects.filter(client=request.user)

    context = {
        'jobs': jobs,
        'total_jobs': jobs.count(),
        'active_jobs': jobs.filter(status='Assigned').count(),
        'completed_jobs': jobs.filter(status='Completed').count(),
    }

    return render(request, 'client/dashboard.html', context)



# POST JOB
@login_required
def post_job(request):

    if request.method == "POST":

        title = request.POST['title']
        description = request.POST['description']
        pay = request.POST['pay']
        location = request.POST['location']

        Job.objects.create(
            title=title,
            description=description,
            pay=pay,
            location=location,
            client=request.user,
            status="Available"
        )

        return redirect('client:dashboard')

    return render(request, 'client/post_job.html')



# VIEW CLIENT JOBS (MY POSTED JOBS PAGE)
@login_required
def client_jobs(request):

    jobs = Job.objects.filter(client=request.user)

    return render(request, 'client/jobs.html', {'jobs': jobs})



# MARK JOB AS COMPLETED
@login_required
def complete_job(request, job_id):

    job = get_object_or_404(Job, id=job_id, client=request.user)

    job.status = "Completed"
    job.save()

    return redirect('client:dashboard')