from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="home"),
    path("tutorials/", views.TutorialList.as_view(), name="tutorial_list"),
    path('<slug:slug>/', views.tutorial_detail, name='tutorial_detail'),
]