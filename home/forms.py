from django import forms
from tutorial.models import Booking, TutorialDate
from datetime import datetime

class BookingForm(forms.ModelForm):
    """
    Form to create a Booking.
    """

# Overriding init function to adjust filtering based on the date of the scheduled event.
# code was taken and appropriated from 
# https://stackoverflow.com/questions/43001425/django-modelform-with-conditions
# https://forum.djangoproject.com/t/queryset-difference/15716
# 
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        current_date = datetime.now()
        print(current_date)
        self.fields['tutorial_date'].queryset = TutorialDate.objects.filter(
            tutorial_date__gte=datetime.now()
            )


    class Meta:
        model = Booking
        fields = ['tutorial_date']

        labels = {
            'tutorial_date': 'Tutorial Date', 
        }