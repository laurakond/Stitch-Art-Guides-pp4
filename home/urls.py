from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.index,
        name="home"
    ),
    path(
        "about/",
        views.about_me,
        name="about"
        ),
    path(
        "book-a-tutorial/",
        views.book_a_tutorial,
        name="book_a_tutorial"
    ),
    path(
        "book-a-tutorial/<slug:slug>/<int:pk>/",
        views.tutorial_session,
        name="tutorial_session"
    ),
    path(
        "my_tutorials/",
        views.my_tutorials,
        name="my_tutorials"
    ),
    path(
        "my_tutorials/delete_booking/<int:booking_id>/",
        views.delete_booking,
        name="delete_booking"
    ),
    path(
        "my_tutorials/edit_booking/<int:booking_id>/",
        views.edit_booking,
        name="edit_booking"
    ),
]
