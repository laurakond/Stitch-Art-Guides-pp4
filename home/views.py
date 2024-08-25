from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def index(request):
    """
    function that displays home page.
    """
    return render(request, "home/index.html")


def about_me(request):
    """
    function that displays about page.
    """
    return render(request, "home/about.html")


def my_tutorials(request):
    """
    function that displays booked tutorial page.
    """
    return render(request, 'home/my_tutorials.html')