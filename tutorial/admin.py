from django.contrib import admin
from .models import Tutorial, TutorialDate, Booking

# Register your models here.

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    """
    Populates filter fields in the database for
    the Tutorial model.
    """
    list_display = ('title', 'tutor_name', 'description')
    list_filter = ('title', 'tutor_name', 'description')
    search_fields = ('title', 'tutor_name', 'description')

@admin.register(TutorialDate)
class TutorialDateAdmin(admin.ModelAdmin):
    """
    Populates filter fields in the database for
    the TutorialDate model.
    """
    list_display = ('tutorial', 'tutorial_date')
    list_filter = ('tutorial', 'tutorial_date')
    search_fields = ('tutorial', 'tutorial_date')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Populates filter fields in the database for
    the Booking model.
    """
    list_display = ('user', 'tutorial_date')
    list_filter = ('user', 'tutorial_date')
    search_fields = ('user', 'tutorial_date')