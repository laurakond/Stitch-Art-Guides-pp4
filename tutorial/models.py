from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Tutorial(models.Model):
    """
    A model that provides information about tutorial
    """
    title = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        max_length=150,
        unique=True
    )
    tutor_name = models.CharField(
        max_length=30,
        unique=False
    )
    description = models.TextField(
        blank=False
    )
    excerpt = models.TextField(
        blank=False
    )
    image = CloudinaryField(
        'image',
        default='placeholder'
    )
    alt_text = models.CharField(
        max_length=150,
        unique=False,
        verbose_name='alt text'
    )
    def __str__(self):
        return f"{self.title}"


class TutorialDate(models.Model):
    """
    A model that sets up the time and date for the tutorials.
    """
    tutorial_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    tutorial = models.ForeignKey(
        Tutorial,
        on_delete=models.CASCADE,
        related_name="selected_tutorial_date"
    )

    def __str__(self):
        return f"{self.tutorial_date} | {self.start_time} | {self.tutorial}"


class Booking(models.Model):
    """
    A model that manages the booking.
    """
    tutorial_date = models.ForeignKey(TutorialDate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tutorial_date} | {self.user}"