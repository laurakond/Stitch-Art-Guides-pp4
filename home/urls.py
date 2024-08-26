from . import views
from django.urls import path

urlpatterns = [
    
    path("", views.index, name="home"),
    path("about/", views.about_me, name="about"),
    path("book_a_tutorial/", views.book_a_tutorial, name="calendar"),
    path("booked_tutorials/", views.my_tutorials, name="booked_tutorials"),
]