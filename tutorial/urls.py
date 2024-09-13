from . import views
from .views import AddTutorial, AddTutorialDate
from django.urls import path


urlpatterns = [
    path("", views.TutorialList.as_view(), name="tutorial_list"),
    path('<slug:slug>/', views.tutorial_detail, name='tutorial_detail'),
    path('tutorials/add_tutorial/', AddTutorial.as_view(), name='add_tutorial'),
]