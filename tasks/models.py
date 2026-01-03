from django.db import models
from django.contrib.auth.models import AbstractUser

from config import settings



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
    

#Task Model
class Task(models.Model):
    PRIORITY_LEVEL = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField(null=True, blank=True)
    priority_level = models.CharField(max_length=20, choices=PRIORITY_LEVEL, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_tasks")
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title