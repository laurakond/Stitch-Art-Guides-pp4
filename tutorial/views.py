from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tutorial, TutorialDate
from .forms import TutorialForm, TutorialDateForm


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
    tutorial_date = TutorialDate.objects.all()

    return render(
        request,
        "tutorial/tutorial_detail.html",
        {"tutorial": tutorial,
         "coach": "Laura K",
         "tutorial_date": tutorial_date,
        },
    )

@login_required
def dashboard_page(request):
    """
    Function to render the main dashboard page.
    """

    if request.user.is_superuser:
        return render(request,
                    "tutorial/dashboard.html",
                    )
    elif not request.user.is_superuser:
        return redirect('account_login')


@login_required
def add_tutorial(request):
    """
    Add tutorial view and generate add tutorial form.
    """

    tutorial_list = Tutorial.objects.all()
    tutorial_form = TutorialForm()

    # handling form post request. This part of the code was appropriated
    # from I blog walkthrough project by Code Institute.
    if request.user.is_superuser:
        if request.method == "POST":
            print("Received a POST request")
            tutorial_form = TutorialForm(data=request.POST)
            if tutorial_form.is_valid():
                tutorial_form.author = request.user
                tutorial_form.save()
                messages.success(
                    request,
                    'New tutorial entry created. You can now add dates and times for it.'
                    )
                return redirect('dashboard')
            else:
                tutorial_form = TutorialForm()
    else:
        messages.error(request,
                       'You do not have access to this content.'
                       )
        return redirect('account_login')

    print("About to render template")
    return render(request,
                  "tutorial/add_tutorial.html",
                  {"tutorial_list": tutorial_list,
                   "tutorial_form":tutorial_form,
                   },
                  )
    

class AddTutorialDate(CreateView):
    """Add Tutorial view"""

    template_name = "tutorial/add_tutorial.html"
    model = TutorialDate
    form_class = TutorialDateForm
    success_url = "/tutorial/"

    def form_valid(self, form):
        form.instance.user = self.request.superuser
        return super(AddTutorialDate, self).form_valid(form)
    
