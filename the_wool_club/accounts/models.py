from django.db import models
from django.contrib.auth.models import User
from learn.models import Workshop, Stitch
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    skill_level = models.TextField(choices=Skill.choices, default = 'Beginner')
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()