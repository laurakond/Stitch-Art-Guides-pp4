from . import views
from django.urls import path


urlpatterns = [
    path("tutorials/", views.TutorialList.as_view(), name="tutorial_list"),
]