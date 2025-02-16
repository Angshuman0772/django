"""
This module contains signal handlers for the User model to automatically create and save a Profile instance whenever a User instance is created or saved.
Functions:
    create_profile(sender, instance, created, **kwargs): Signal handler that creates a Profile instance when a new User instance is created.
    save_profile(sender, instance, **kwargs): Signal handler that saves the associated Profile instance whenever a User instance is saved.
"""
# We are connecting the signal handlers to the User model's post_save signal to ensure that a Profile is created and saved automatically.

from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

def save_profile(sender, instance, **kwargs):
    instance.profile.save()