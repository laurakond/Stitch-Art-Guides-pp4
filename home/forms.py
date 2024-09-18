from django import forms
from tutorial.models import Booking, TutorialDate
from datetime import datetime

class BookingForm(forms.ModelForm):
    """
    Form to create a Booking.
    """

    def __init__(self, *args, **kwargs):
        # grabbing the user from the arguments and storing in a separate parameter
        self.user = kwargs.pop('user', None)
        current_date = datetime.now()

        # filter Tutorial dates/times that do not have a booking created.
        future_tutorials = TutorialDate.objects.filter(
            tutorial_date__gte=current_date
            ).exclude(booking__isnull=False)
        
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