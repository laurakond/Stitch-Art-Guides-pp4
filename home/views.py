from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from tutorial.models import Booking, TutorialDate, Tutorial
from .forms import BookingForm


def index(request):
    """
    Function that displays the home page.
    **Template:**
        :template:`home/index.html`
    """
    return render(request, "home/index.html")


def about_me(request):
    """
    Function that displays the About page.
    **Template:**
    :template:`home/about.html`
    """
    return render(request, "home/about.html")


# The below code was appropriated from Code Institute's
# July Hackathon United Events team repository:
# https://github.com/hannahro15/July24Hackathon-United-Events
def book_a_tutorial(request):
    """
    Function that displays calendar for booking a tutorial.
    **Context**
    ``tutorials``
        All instances of tutorials of :model:`tutorial.TutorialDate`
    ``events``
        A list of events stating information from :model:
        `tutorial.TutorialDate`
    ``is_booked``
        Checks if the tutorial instance is booked.
    **Template:**
        :template:`home/book_tutorial.html`
    """

    if not request.user.is_authenticated:
        messages.error(
            request,
            'You do not have access to this content. Please sign up or sign in.'
        )
        return redirect(f"{reverse('account_login')}?next={request.path}")

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


def tutorial_session(request, slug, pk):
    """
    Function that captures the Tutorial Date primary key
    and Tutorial slug and loads appropriate view.
    **Context**
    ``event_slot``
        An instance of tutorial dates of :model:`tutorial.TutorialDate`
    ``event_datetime``
        Combines each instance date and time of :model:`tutorial.TutorialDate`
    ``is_booked``
        Checks if the tutorial instance is booked.
    **Template:**
        :template:`home/tutorial_session.html`
    """
    # tutorial__slug captures the slug from the Tutorial Model.
    # Full reference noted in the README.md.
    event_slot = get_object_or_404(TutorialDate, pk=pk, tutorial__slug=slug)

    if not request.user.is_authenticated:
        messages.error(
            request,
            'You do not have access to this content. Please sign up or sign in.'
            )
        return redirect(f"{reverse('account_login')}?next={request.path}")

    # verify if the event date is the same as the current date
    current_datetime = datetime.now()
    event_datetime = datetime.combine(
        event_slot.tutorial_date,
        event_slot.start_time)

    # compare the current date to the event date and raise
    # an appropriate message
    if event_datetime < current_datetime:
        messages.error(
            request,
            'This event has now passed and cannot be accessed.'
        )
        return redirect('book_a_tutorial')

    # checks if a tutorial is already booked, generates
    # appropriate message & redirects to the calendar view
    is_booked = Booking.objects.filter(tutorial_date=event_slot).exists()
    if is_booked:
        messages.error(
            request,
            'This tutorial is already booked. Choose another date.'
        )
        return redirect('book_a_tutorial')

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
        {
            "event_slot": event_slot,
            "is_booked": is_booked,
        },
        )


def my_tutorials(request):
    """
    Function that displays past and future tutorial bookings
    and renders My Tutorials page.
    **Context**
    ``bookings``
        All bookings of a user of :model:`tutorial.Booking`
    ``current_datetime``
        Current date
    ``past_sessions``
        List of all past booked Tutorials of :model:`tutorial.Booking`
    ``upcoming_sessions``
        List of all future booked Tutorials of :model:`tutorial.Booking`
    **Template:**
        :template:`home/my_tutorials.html`
    """
    if not request.user.is_authenticated:
        messages.error(
            request,
            'You do not have access to this content. Please sign up or sign in.'
            )
        return redirect(f"{reverse('account_login')}?next={request.path}")

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
        {
            "past_sessions": past_sessions,
            "upcoming_sessions": upcoming_sessions,
        }
        )


def edit_booking(request, booking_id):
    """
    Function that edits the tutorial booking.
    **Context**
    ``booking``
        All bookings of a user of :model:`tutorial.Booking`
    ``tutorial_date``
        An instance of tutorial date's booking of :model:
        `tutorial.TutorialDate`
    ``tutorial``
        An instance of tutorial's booking of :model:`tutorial.Tutorial`
    ``available_tutorials``
        List of all available Tutorial instances of :model:
        `tutorial.TutorialDate`
    ``other_tutorials``
        List of all other Tutorial instances of :model:`tutorial.TutorialDate`
    ``tutorial_form``
        An instance of :form:`home.BookingForm`
    ``tutorial_list``
        List of all bookings of :model:`tutorial.Booking`
    **Template:**
        :template:`home/edit_booking.html`
    """

    # Check if the user is logged in, and if not, redirect to the login page.
    if not request.user.is_authenticated:
        messages.error(
            request,
            'You do not have access to this content. Please sign up or sign in.'
            )
        return redirect(f"{reverse('account_login')}?next={request.path}")

    # Fetch if each booking instance exists & if it doesn't return an alert
    # message
    try:
        booking = Booking.objects.get(pk=booking_id)
    except Booking.DoesNotExist:
        messages.add_message(
            request,
            messages.ERROR,
            "Booking does not exist."
        )
        return redirect('my_tutorials')

    # Validates the user is the logged in user and returns approapriate message
    if booking.user != request.user:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have permission to access this booking.'
        )
        return redirect('my_tutorials')

    # message filtering functionality based on booked tutorials has been
    # implemented with guidance from Sarah, Code Institute's
    # Tutor support team.

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
            messages.error(
                request,
                'You can only edit your own bookings.'
            )
            return redirect('my_tutorials')
    else:
        tutorial_form = BookingForm(instance=booking)

    return render(
        request,
        "home/edit_booking.html",
        {
            "booking": booking,
            "tutorial_list": tutorial_list,
            "tutorial_form": tutorial_form,
            "available_tutorials": available_tutorials,
            "other_tutorials": other_tutorials,
        },
    )


# This part of code was appropriated from the Code Institute's
# blog walkthrough
@login_required
def delete_booking(request, booking_id):
    """
    Function that deletes the tutorial booking.
    **Context**
    ``booking``
        An instance of a booking of :model:`tutorial.Booking`
    **Template:**
        :template:`home/edit_booking.html`
    """

    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.user == request.user:
        booking.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Booking deleted')
        return redirect('my_tutorials')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own bookings.'
        )
        return redirect('my_tutorials')
