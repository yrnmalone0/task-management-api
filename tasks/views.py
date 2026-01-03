from django.shortcuts import render
from . serializers import UserRegistrationSerializer, UpdateUserProfileSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task


#register users
@api_view(['POST'])
def register_user(request):
    #validate incoming data before touching the database
    serializer = UserRegistrationSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#update user profile
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user  #get the currently logged-in user
    serializer = UpdateUserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#create a task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    user = request.user #get currently logged user
    serializer = TaskSerializer(data=request.data) #pass content or payload to serializer
    if serializer.is_valid(): #check if data is valid
        serializer.save(creator=user) #save and set logged in to creator
        return Response(
            {
                "message": "Task created successfully!",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#view tasks
@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


#view task details or single task
@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            {"error": "Task not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = TaskSerializer(task)
    return Response(serializer.data)