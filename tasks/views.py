from django.shortcuts import render
from . serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



#register users
@api_view(['POST'])
def register_user(request):
    #validate incoming data before touching the database
    serializer = UserRegistrationSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
