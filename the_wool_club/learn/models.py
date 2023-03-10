from django.db import models

# Create your models here.

class Workshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField()
    cost = models.IntegerField()
    keywords = models.TextField()
    skill_level = models.TextField()
    location = models.TextField()