from django.contrib import admin
from .models import Tutorial, TutorialDate, Booking

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(TutorialDate)
admin.site.register(Booking)