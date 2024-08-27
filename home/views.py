from django.shortcuts import render, get_object_or_404
from django.views import generic
from tutorial.models import Booking


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
    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        'home/my_tutorials.html',
        {"bookings": bookings,}
         )


# the below code was appropriated from Code 
# Institute's Blog walkthrough
def book_a_tutorial(request):
    """
    Function that displays calendar for booking a tutorial.
    """

    return render(
        request,
        "home/book_tutorial.html",
    )
