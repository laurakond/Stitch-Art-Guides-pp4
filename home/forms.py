from datetime import datetime
from django import forms
from tutorial.models import Booking, TutorialDate


class BookingForm(forms.ModelForm):
    """Form to create a Booking."""

    def __init__(self, *args, **kwargs):
        current_date = datetime.now()
        current_time = current_date.time()

        # filter Tutorial dates/times that do not have a booking created.
        free_tutorials = TutorialDate.objects.filter(
            tutorial_date__gt=current_date
            ).exclude(booking__isnull=False)

        # tutorials happening today only
        free_tutorials_today = TutorialDate.objects.filter(
            tutorial_date=current_date,
            start_time__gte=current_time,
            ).exclude(booking__isnull=False)

        # combine both filters into one
        future_tutorials = free_tutorials | free_tutorials_today

        # Override __init__ function to show results based on
        # applied conditional filtering above. The code was
        # appropriated from
        # https://forum.djangoproject.com/t/queryset-difference/15716
        # https://stackoverflow.com/questions/43001425/django-modelform-with-conditions
        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields['tutorial_date'].queryset = future_tutorials

    class Meta:
        model = Booking
        fields = ['tutorial_date']

        labels = {
            'tutorial_date': 'Tutorial Date',
        }
