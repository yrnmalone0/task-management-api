from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register_user, name="register_user"),
    path('update_profile/', views.update_user_profile, name="update_user_profile"),
]