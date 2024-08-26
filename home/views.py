from django.shortcuts import render, get_object_or_404
from django.views import generic
from tutorial.models import Booking
import calendar
from calendar import HTMLCalendar
from datetime import datetime

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
    #tutorial_date = TutorialDate.objects.all()

    return render(
        request,
        'home/my_tutorials.html',
        {"bookings": bookings,}
         )


# the below code was appropriated from Code 
# Institute's Blog walkthrough
def book_a_tutorial(request,  
                    year=datetime.now().year, 
                    month=datetime.now().strftime('%B')):
    """
    Function that displays calendar for booking a tutorial.
    """
    # the below code was appropriated from 
    # codemy.com Youtube tutorial: 
    # https://www.youtube.com/watch?v=4EJlrweJE-M&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=3
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # create a calendar
    tutorial_calendar = HTMLCalendar().formatmonth(year, month_number)

    return render(
        request,
        "home/book_tutorial.html",
        {"tutorial_calendar": tutorial_calendar,
         "month_number": month_number,
        },
    )