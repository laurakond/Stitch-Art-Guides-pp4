from django.shortcuts import render
from django.views import generic
from .models import Tutorial, TutorialDate

# Create your views here.

class TutorialList(generic.ListView):
    queryset = Tutorial.objects.all()
    template_name = "tutorial_list.html"