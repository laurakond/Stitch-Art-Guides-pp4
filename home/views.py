from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def about_me(request):
    return render(request, "home/about.html")