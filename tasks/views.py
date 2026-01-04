from django.shortcuts import render
from . serializers import UserRegistrationSerializer, UpdateUserProfileSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Task
from django.utils import timezone


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



#update a task (only edited by authenticated users/creators of that task)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, pk):
    user = request.user
    task = Task.objects.get(id=pk)
    if task.completed:
        return Response(
            {"error": "Task is completed and cannot be edited. Revert to incomplete to edit."},
            status=status.HTTP_400_BAD_REQUEST
        )
    if task.creator != user:
        return Response(
            {"message": "You're not the creator of this task."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Task updated successfully!",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#Delete a task (only authenticated users can delete a task the created)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    user = request.user
    task = Task.objects.get(id=pk)
    if task.creator != user:
        return Response(
            {"error": "You're not the creator of this task and not authorized to delete"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    task.delete()
    return Response(
        {"message": "Task deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


# Mark a task complete or incomplete (only creator can change)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_task_complete(request, pk):
    user = request.user
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

    if task.creator != user:
        return Response(
            {"error": "You're not the creator of this task and not authorized to change its completion status"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Accept explicit 'completed' boolean in payload, or toggle if omitted
    completed = request.data.get('completed', None)
    if completed is None:
        # toggle
        if not task.completed:
            task.completed = True
            task.completed_at = timezone.now()
            task.status = 'Completed'
        else:
            task.completed = False
            task.completed_at = None
            task.status = 'Pending'
    else:
        # coerce to boolean for common string/number forms
        if isinstance(completed, str):
            completed_val = completed.lower() in ['true', '1', 'yes']
        else:
            completed_val = bool(completed)

        if completed_val:
            task.completed = True
            task.completed_at = timezone.now()
            task.status = 'Completed'
        else:
            task.completed = False
            task.completed_at = None
            task.status = 'Pending'

    task.save()
    serializer = TaskSerializer(task)
    return Response(
        {"message": "Task completion status updated", "data": serializer.data}, status=status.HTTP_200_OK
    )