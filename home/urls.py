from . import views
from django.urls import path

urlpatterns = [
    
    path("", views.index, name="home"),
    path("about/", views.about_me, name="about"),
    path("book-a-tutorial/", views.book_a_tutorial, name="calendar"),
    path("book-a-tutorial/<slug:slug>/<int:pk>/", views.tutorial_session, name="tutorial_slot"),
    path("booked-tutorials/", views.my_tutorials, name="booked_tutorials"),
    path("booked-tutorials/delete_booking/<int:booking_id>/", views.delete_booking, name="delete_booking"),
]