from . import views
from django.urls import path


urlpatterns = [
    path("", views.TutorialList.as_view(), name="tutorial_list"),
]