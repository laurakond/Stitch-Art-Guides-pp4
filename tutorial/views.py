from django.shortcuts import render
from django.views import generic
from .models import Tutorial, TutorialDate

# Create your views here.
class TutorialList(generic.ListView):
    queryset = Tutorial.objects.all()
    template_name = "tutorial/tutorial_list.html"


def index(request):
    return render(request, "tutorial/index.html")