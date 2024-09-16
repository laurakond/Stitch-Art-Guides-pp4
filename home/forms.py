from django import forms
from tutorial.models import TutorialDate

class TutorialDateForm(forms.ModelForm):
    """
    Form to create a Tutorial Date.
    """
    class Meta:
        model = TutorialDate
        fields = ['tutorial', 'tutorial_date','start_time']

        widgets = {
            'tutorial_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            # 'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

        labels = {
            'tutorial': 'Select Tutorial', 
            'tutorial_date': 'Tutorial Date', 
            'start_time': 'Tutorial Start Time', 
            # 'end_time': 'Tutorial End Time', 
        }
