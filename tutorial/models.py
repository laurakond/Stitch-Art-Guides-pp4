from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutorial(models.Model):
    """
    A model that provides information about tutorial
    """
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    tutor_name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    date = models.TextField(blank=True)
    time = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"