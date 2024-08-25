from . import views
from django.urls import path

urlpatterns = [
    
    path("", views.index, name="home"),
    path("about/", views.about_me, name="about"),
    path("booked_tutorials/", views.my_tutorials, name="booked_tutorials"),
]