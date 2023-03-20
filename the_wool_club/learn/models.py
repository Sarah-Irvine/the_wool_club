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
    duration = models.IntegerField(default=3)

    def __str__(self):
        return self.title

class BasicArticle(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Stitch(models.Model):

    class Skill(models.TextChoices):
        ONE = 'Beginner'
        TWO = 'Intermediate'
        THREE = 'Advanced'

    stitch = models.TextField()
    skill_level = models.TextField(choices=Skill.choices)
    description = models.TextField(blank=True, null=True)
    how_to = models.TextField(blank=True, null=True)
    image = models.ImageField(default='knitting_steps.jpeg')

    def __str__(self):
        return self.stitch


