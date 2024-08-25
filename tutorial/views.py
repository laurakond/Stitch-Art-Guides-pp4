from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tutorial, TutorialDate
import calendar
from calendar import HTMLCalendar
from datetime import datetime


# Create your views here.
class TutorialList(generic.ListView):
    """
    Class that displays all tutorials in one page.
    """
    queryset = Tutorial.objects.all()
    template_name = "tutorial/tutorial_list.html"


# the below code was appropriated from Code 
# Institute's Blog walkthrough
def tutorial_detail(request, 
                    slug, 
                    year=datetime.now().year, 
                    month=datetime.now().strftime('%B')):
    """
    Function that displays individual tutorial's details.
    """

    queryset = Tutorial.objects.all()
    tutorial = get_object_or_404(queryset, slug=slug)
    tutorial_date = TutorialDate.objects.all()

    # the below code was appropriated from 
    # codemy.com Youtube tutorial: 
    # https://www.youtube.com/watch?v=4EJlrweJE-M&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=3
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # create a calendar
    tutorial_calendar = HTMLCalendar().formatmonth(year, month_number)

    return render(
        request,
        "tutorial/tutorial_detail.html",
        {"tutorial": tutorial,
         "coach": "Laura K",
         "tutorial_date": tutorial_date,
         "tutorial_calendar": tutorial_calendar,
         "month_number": month_number,
        },
    )
