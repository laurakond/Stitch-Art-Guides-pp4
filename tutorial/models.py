from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutorial(models.Model):
    """
    A model that provides information about tutorial
    """
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    tutor_name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=False)
    excerpt = models.TextField(blank=False)
    tutorial_date = models.DateTimeField(default='2024-08-17 00:10:00', null=False, blank=False)

    def __str__(self):
        return f"{self.title}"


