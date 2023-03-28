from django.db import models
from django.contrib.auth.models import User
from learn.models import Workshop, Stitch


class UserProfile(models.Model):

    class Skill(models.TextChoices):
        BEGINNER = 'Beginner'
        INTERMEDIATE = 'Intermediate'
        ADVANCED = 'Advanced'
        
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    attending = models.ManyToManyField(
        Workshop, blank=True, related_name="attending")
    saved = models.ManyToManyField(
        Stitch, blank=True, related_name="saved")
    profile_pic = models.ImageField(default='profile_images/sheep.jpg', upload_to='profile_images/')
    bio = models.TextField(null=True, blank=True)
    skill_level = models.TextField(choices=Skill.choices, default = 'Beginner')
    
    def __str__(self):
        return self.user.username

