from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register_user, name="register_user"),
    path('update_profile/', views.update_user_profile, name="update_user_profile"),
    path('create_task/', views.create_task, name="create_task"),
    path('task_list', views.task_list, name="task_list")
]