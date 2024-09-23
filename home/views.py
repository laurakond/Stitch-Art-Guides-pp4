from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import datetime
from tutorial.models import Booking, TutorialDate, Tutorial
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
    # Fetch each booking instance for the logged in user
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    
    # message filtering functionality based on booked tutorials has been
    # implemented with guidance from Sarah, Code Institute's
    # Tutor support team (lines 152-178 & 204-212).

    # Fetch the tutorial the user has booked
    tutorial_date = get_object_or_404(
        TutorialDate,
        pk=booking.tutorial_date.id
        )
    tutorial = get_object_or_404(
        Tutorial,
        pk=tutorial_date.tutorial.id
        )
    # Get current date for filtering for the future
    date_now = datetime.now()
    
    # Filter available TutorialDates by this tutorial,
    # bookings and future dates
    available_tutorials = TutorialDate.objects.filter(
        tutorial=tutorial,
        booking__isnull=True,
        tutorial_date__gte=date_now
        )
    
    # Filter available TutorialDates by this tutorial,
    # bookings and future dates
    other_tutorials = TutorialDate.objects.filter(
        booking__isnull=True,
        tutorial_date__gte=date_now
        ).exclude(tutorial=tutorial)
    
    print(f"Available tutorials for this tutorial: {available_tutorials}")
    print(f"All available tutorials: {other_tutorials}")

    # generate a form based on the booking instance
    tutorial_form = BookingForm(instance=booking)
    tutorial_list = Booking.objects.all()

    if request.method == "POST":
        tutorial_form = BookingForm(data=request.POST, instance=booking)
        if tutorial_form.is_valid():
            tutorial_form.author = request.user
            tutorial_form.save()
            messages.success(
                request,
                'Your booking has been updated.'
                )
            return redirect('my_tutorials')
        else:
            messages.error(request,
                       'You can only edit your own bookings.'
                       )
            return redirect('my_tutorials')
    else:
        tutorial_form = BookingForm(instance=booking)
    
    # Based on the number of available bookings for this or other tutorials are 0
    # show appropriate message
    if len(available_tutorials) == 0 and len(other_tutorials) == 0:
        messages.error(request, "No available dates for all tutorials. Come back later to check.")
    elif len(available_tutorials) == 0:
        messages.error(request,
        "No other available dates for this tutorial."
        " Feel free to choose another though!")
    elif len(available_tutorials) > 0 and len(other_tutorials) == 0:
        messages.error(request,
        "Choose another date for your tutorial.")    
    else:
        messages.error(request,
        "Pick another date or choose a different tutorial.")

    return render(request,
                "home/edit_booking.html",
                {"booking": booking,
                "tutorial_list": tutorial_list,
                "tutorial_form":tutorial_form,
                "available_tutorials": available_tutorials,
                "other_tutorials": other_tutorials,},
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
    