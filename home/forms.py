from django import forms
from tutorial.models import Booking


class BookingForm(forms.ModelForm):
    """
    Form to create a Booking.
    """
    class Meta:
        model = Booking
        fields = ['tutorial_date']

        # widgets = {
        #     'tutorial_date': forms.ModelChoiceField()
        # }

        labels = {
            'tutorial_date': 'Tutorial Date', 
        }