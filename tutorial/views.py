from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tutorial, TutorialDate

# Create your views here.
class TutorialList(generic.ListView):
    queryset = Tutorial.objects.all()
    template_name = "tutorial/tutorial_list.html"


def index(request):
    return render(request, "tutorial/index.html")

# the below code was appropriated from Code 
# Institute's Blog walkthrough
def tutorial_detail(request, slug):
    "function that displays individual tutorial's details"

    queryset = Tutorial.objects.all()
    tutorial = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "tutorial/tutorial_detail.html",
        {"tutorial": tutorial,
         "coach": "Laura K"},
    )