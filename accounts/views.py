from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

def register_role(request):
    return render(request,'accounts/register_role.html')

def register_client(request):
    return render(request, 'accounts/register_client.html')

def register_worker(request):
    return render(request, 'accounts/register_worker.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def password_reset_view(request):
    return render(request, 'accounts/password_reset.html')

