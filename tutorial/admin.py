from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tutorial, TutorialDate, Booking


@admin.register(Tutorial)
class TutorialAdmin(SummernoteModelAdmin):
    """
    Populates filter fields in the database for
    the Tutorial model.
    """
    list_display = ('title', 'slug', 'tutor_name', 'excerpt')
    list_filter = ('title', 'tutor_name')
    search_fields = ('title', 'slug', 'tutor_name', 'description', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


@admin.register(TutorialDate)
class TutorialDateAdmin(SummernoteModelAdmin):
    """
    Populates filter fields in the database for
    the TutorialDate model.
    """
    list_display = ('tutorial_date', 'start_time', 'tutorial')
    list_filter = ('tutorial_date', 'start_time', 'tutorial')
    search_fields = ('tutorial_date', 'tutorial')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Populates filter fields in the database for
    the Booking model.
    """
    list_display = ('tutorial_date', 'user')
    list_filter = ('tutorial_date', 'user')
    search_fields = ('tutorial_date', 'user')
