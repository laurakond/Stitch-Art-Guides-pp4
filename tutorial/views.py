from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_tutorial(request):
    return HttpResponse("Created new app")