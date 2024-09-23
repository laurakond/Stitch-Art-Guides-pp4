"""stitch art guides project URL configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import error_400, error_403, error_404, error_500


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        "accounts/",
        include("allauth.urls")
    ),
    path(
        'summernote/',
        include('django_summernote.urls')
    ),
    path(
        'tutorials/',
        include("tutorial.urls"),
        name="tutorial-urls"
    ),
    path(
        '',
        include("home.urls"),
        name="home-urls"
    ),
]


"""Error handlers"""
handler400 = error_400
handler403 = error_403
handler404 = error_404
handler500 = error_500
