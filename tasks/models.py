from django.db import models
from django.contrib.auth.models import AbstractUser



#Custom User Model
class CustomUser(AbstractUser):
    """Extended User Model"""
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) #set field to current date/time when the object is first created
    updated_at = models.DateTimeField(auto_now=True) #update automatically on every .save()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username