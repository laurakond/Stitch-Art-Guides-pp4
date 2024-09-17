from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import datetime
from tutorial.models import Booking, TutorialDate
from .forms import BookingForm


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


# The below code was appropriated from Code Institute's
# July Hackathon United Events team repository:
# https://github.com/hannahro15/July24Hackathon-United-Events
def book_a_tutorial(request):
    """
    Function that displays calendar for booking a tutorial.
    """
    tutorials = TutorialDate.objects.all()
    events = []
    for tutorial in tutorials:
        is_booked = Booking.objects.filter(tutorial_date=tutorial).exists()
        events.append({
            'title': tutorial.tutorial.title,
            'start_date': tutorial.tutorial_date.isoformat(),
            'start_time': tutorial.start_time.strftime('%H:%M'),
            'end_time': tutorial.end_time.strftime('%H:%M'),
            'pk': tutorial.pk,
            'slug': tutorial.tutorial.slug,
            'is_booked': is_booked,
        })

    return render(
        request,
        "home/book_tutorial.html",
        {"events": events},
    )


@login_required
def tutorial_session(request, slug, pk):
    """
    Function that captures the Tutorial Date primary key
    and Tutorial slug and loads appropriate view.
    """
    # tutorial__slug captures the slug from the Tutorial Model.
    # Full reference noted in the README.md.
    event_slot = get_object_or_404(TutorialDate, pk=pk, tutorial__slug=slug)

    # verify if the event date is the same as the current date
    current_datetime = datetime.now()
    event_datetime = datetime.combine(
        event_slot.tutorial_date,
        event_slot.start_time)

    # compare the current date to the event date and raise
    # an appropriate message
    if event_datetime < current_datetime:
        if not request.user.is_authenticated:
            messages.error(request,
                           'Please log in to access the details.')
            return redirect('login')
        else:
            messages.error(request,
                           'This event has now passed and cannot be accessed.')
            return redirect('book_a_tutorial')

    # checks if a tutorial is already booked, generates
    # appropriate message & redirects to the calendar view
    is_booked = Booking.objects.filter(tutorial_date=event_slot).exists()
    if is_booked:
        messages.error(request,
                        'This tutorial is already booked. Choose another date.')
        return redirect('calendar')
        
    # requesting a booking for the tutorial slot
    if request.method == "POST" and not is_booked:
        user = request.user
        Booking.objects.create(user=user, tutorial_date=event_slot)
        messages.add_message(
            request, messages.SUCCESS,
            'Your tutorial is booked. See you then!'
            )
        return redirect('my_tutorials')

    return render(
        request,
        "home/tutorial_session.html",
        {"event_slot": event_slot, 
         "is_booked": is_booked,},
        )


@login_required
def my_tutorials(request):
    """
    Function that displays past and future tutorial bookings
    and renders My Bookings page.
    """
    bookings = Booking.objects.filter(user=request.user.id)
    current_datetime = datetime.now()
    past_sessions = []
    upcoming_sessions = []

    # loops through each booking and checks if each
    # booking date is before or after the current date.
    for booking in bookings:
        event_datetime = datetime.combine(
            booking.tutorial_date.tutorial_date,
            booking.tutorial_date.start_time
            )
        if event_datetime > current_datetime:
            upcoming_sessions.append(booking)
        elif event_datetime < current_datetime:
            past_sessions.append(booking)

    return render(
        request,
        'home/my_tutorials.html',
        {"past_sessions": past_sessions,
         "upcoming_sessions": upcoming_sessions,
         }
        )


@login_required
def edit_booking(request, booking_id):
    """
    Function that edits the tutorial booking.
    """
    # tutorial_date__tutorial__slug=slug allows to access the slug from
    # the Tutorial model so that the url path can be accessed based on
    # the booking instance.
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    tutorial_form = BookingForm(instance=booking)
    tutorial_list = Booking.objects.all()
    # if request.method == "POST":
    #     tutorial_form = BookingForm(data=request.POST)
    #         if tutorial_form.is_valid():
    #             tutorial_form.author = request.user
    #             tutorial_form.save()
    #             messages.success(
    #                 request,
    #                 'New tutorial date & time entry created.'
    #                 )
    #             return redirect('my_tutorials')
    #         else:
    #             tutorial_form = TutorialDateForm()
    # else:
    #     messages.error(request,
    #                    'You can only edit your own bookings.'
    #                    )
    #     return redirect('my_tutorials')      

    return render(request,
                "home/edit_booking.html",
                {"booking": booking,
                "tutorial_list": tutorial_list,
                "tutorial_form":tutorial_form,},
                #   {"bookings": bookings,
                #    "tutorial_list": tutorial_list,
                #    "form": form,
                #    },
                )


# This part of code was appropriated from the Code Institute's 
# blog walkthrough
@login_required
def delete_booking(request, booking_id):
    """
    Function that deletes the tutorial booking.
    """
    
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.user == request.user: 
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted')
        return redirect('my_tutorials')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own bookings.')
        return redirect('my_tutorials')
    