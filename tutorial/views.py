from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tutorial, TutorialDate

# Create your views here.
class TutorialList(generic.ListView):
    """
    Class that displays all tutorials in one page.
    """
    queryset = Tutorial.objects.all()
    template_name = "tutorial/tutorial_list.html"


# the below code was appropriated from Code 
# Institute's Blog walkthrough
def tutorial_detail(request, slug):
    """
    Function that displays individual tutorial's details.
    """

    queryset = Tutorial.objects.all()
    tutorial = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "tutorial/tutorial_detail.html",
        {"tutorial": tutorial,
         "coach": "Laura K"},
    )