from django.shortcuts import render, get_object_or_404
from django.views import generic
from tutorial.models import Booking, TutorialDate, Tutorial


# Create your views here.
def index(request):
    """
    Function that displays the home page.
    """
    return render(request, "home/index.html")


def about_me(request):
    """
    Function that displays the About page.
    """
    return render(request, "home/about.html")


def my_tutorials(request):
    """
    Function that displays booked tutorial page.
    """
    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        'home/my_tutorials.html',
        {"bookings": bookings,}
        )


def test_me(request,pk):
    """
    Function that captures the Tutorial Date primary key
    and loads appropriate view.
    """
    # queryset = TutorialDate.objects.all()
    tutorial_date_pk = get_object_or_404(TutorialDate, pk=pk)
    tutorial_pk = tutorial_date_pk
    return render(
        request, 
        "home/test.html", 
        {"tutorial_pk": tutorial_pk,},
        )



# the below code was appropriated from Code Institute's 
# July Hackathon United Events team repository:
# https://github.com/hannahro15/July24Hackathon-United-Events
def book_a_tutorial(request):
    """
    Function that displays calendar for booking a tutorial.
    """

    tutorials = TutorialDate.objects.all()
    events = []
    for tutorial in tutorials:
        events.append({
            'title': tutorial.tutorial.title,
            'start_date': tutorial.tutorial_date.isoformat(),
            'start_time': tutorial.start_time.strftime('%H:%M'),
            'end_time': tutorial.end_time.strftime('%H:%M'),
            'pk': tutorial.pk,
        })
   
    return render(
        request,
        "home/book_tutorial.html",
        {"events": events},
    )
