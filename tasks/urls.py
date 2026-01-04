from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register_user, name="register_user"),
    path('update_profile/', views.update_user_profile, name="update_user_profile"),
    path('create_task/', views.create_task, name="create_task"),
    path('tasks', views.task_list, name="tasks"),
    path('task/<int:pk>/', views.task_detail, name="task_detail"),
    path('update_task/<int:pk>/', views.update_task, name="update_task"),
    path('delete_task/<int:pk>/', views.delete_task, name="delete_task"),
]