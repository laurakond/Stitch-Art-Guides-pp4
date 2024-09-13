from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Tutorial, TutorialDate

class TutorialForm(forms.ModelForm):
    """
    Form to create a Tutorial
    """
    class Meta:
        model = Tutorial
        fields = ['title', 'slug', 'description', 'tutor_name', 'excerpt',]

        widgets = {
            'description': SummernoteWidget(),
            'excerpt': SummernoteWidget(),
        }

        labels = {
            'title': 'Tutorial Title',
            'description': 'Tutorial Description',
            'tutor_name': 'Tutor Name', 
            'excerpt': 'Tutorial Excerpt', 
            # 'tutorial_date': 'Tutorial Date', 
            # 'tutorial_start_time': 'Tutorial Start Time', 
            # 'tutorial_end_time': 'Tutorial End Time', 
            # 'image': 'Tutorial Image', 
            # 'image_alt': 'Image Description',
        }

class TutorialDateForm(forms.ModelForm):
    """
    Form to create a Tutorial Date.
    """
    class Meta:
        model = TutorialDate
        fields = ['tutorial_date','start_time','end_time']

        # widgets = {
        #     'description': SummernoteWidget(),
        #     'excerpt': SummernoteWidget(),
        # }

        labels = {
            'tutorial_date': 'Tutorial Date', 
            'start_time': 'Tutorial Start Time', 
            'end_time': 'Tutorial End Time', 
            # 'image': 'Tutorial Image', 
            # 'image_alt': 'Image Description',
        }