from . import views
# from .views import AddTutorial, AddTutorialDate
from django.urls import path


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('add_tutorial/', views.add_tutorial, name='add_tutorial'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
    path('add_tutorial_date/', views.add_tutorial_date, name='add_tutorial_date'),
    path('delete_tutorial_date/', views.delete_tutorial_date, name='delete_tutorial_date'),
]
