from . import views
# from .views import AddTutorial, AddTutorialDate
from django.urls import path


urlpatterns = [
    path("", views.TutorialList.as_view(), name="tutorial_list"),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('dashboard/add_tutorial/', views.add_tutorial, name='add_tutorial'),
    path('<slug:slug>/', views.tutorial_detail, name='tutorial_detail'),
]