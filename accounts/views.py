from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import ClientProfile, WorkerProfile

User = get_user_model()


# ROLE SELECTION
def register_role(request):
    return render(request, 'accounts/register_role.html')


# CLIENT REGISTRATION
def register_client(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('register_client')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            role='client'
        )

        ClientProfile.objects.create(
            user=user,
            full_name=full_name,
            phone_number=phone_number,
            location=location
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'accounts/register_client.html')

# WORKER REGISTRATION
def register_worker(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        primary_skill = request.POST['primary_skill']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('register_worker')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            role='worker'
        )

        WorkerProfile.objects.create(
            user=user,
            full_name=full_name,
            phone_number=phone_number,
            location=location,
            primary_skill=primary_skill
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'accounts/register_worker.html')

# LOGIN
def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']   # login form uses email as username
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            # Role-based redirect
            if user.role == 'client':
                return redirect('client:dashboard')
            elif user.role == 'worker':
                return redirect('worker:worker_dashboard')

        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'accounts/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('landing')