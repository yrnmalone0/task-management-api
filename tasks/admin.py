from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser, Task



#register custom-user and display on Django-Admin
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "bio", "profile_picture", "created_at", "updated_at")
admin.site.register(CustomUser, CustomUserAdmin)


#register Task model on Django-Admin
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "due_date", "priority_level", "status", "creator", "completed", "completed_at", "created_at", "updated_at")
admin.site.register(Task, TaskAdmin)
