from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def placeholder(request):
    return HttpResponse("This app is working.")