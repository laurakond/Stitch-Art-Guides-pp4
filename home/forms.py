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

        # use reverse relationship to access the user from the views.py booking variable
        # and assigning it to the user to remove from shown options
        future_tutorials = TutorialDate.objects.filter(
            tutorial_date__gte=current_date
            ).exclude(booking__user=self.user)
        
        # Overriding init function to adjust filtering based on the date of the scheduled event.
        # Code was appropriated from 
        # https://stackoverflow.com/questions/43001425/django-modelform-with-conditions
        # https://forum.djangoproject.com/t/queryset-difference/15716
        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields['tutorial_date'].queryset = future_tutorials

    class Meta:
        model = Booking
        fields = ['tutorial_date']

        labels = {
            'tutorial_date': 'Tutorial Date', 
        }