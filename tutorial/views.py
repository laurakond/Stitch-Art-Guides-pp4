from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tutorial, TutorialDate


class TutorialList(generic.ListView):
    """
    Class that displays all tutorials in one page.
    **Context**
    ``queryset``
        All displayed instances of :model:`tutorial.Tutorial`
    **Template:**
    :template:`tutorial/tutorial_list.html`
    """
    queryset = Tutorial.objects.all()
    template_name = "tutorial/tutorial_list.html"


# the below code was appropriated from Code
# Institute's Blog walkthrough
def tutorial_detail(request, slug):
    """
    Function that displays individual tutorial's details.
    **Context**
    ``tutorial``
        An individual tutorial of :model:`tutorial.Tutorial`
    ``tutorial_date``
        An individual tutorial of :model:`tutorial.TutorialDate`
    **Template:**
        :template:`tutorial/tutorial_detail.html`
    """

    queryset = Tutorial.objects.all()
    tutorial = get_object_or_404(queryset, slug=slug)
    tutorial_date = TutorialDate.objects.all()

    return render(
        request,
        "tutorial/tutorial_detail.html",
        {
            "tutorial": tutorial,
            "tutorial_date": tutorial_date,
        },
    )
