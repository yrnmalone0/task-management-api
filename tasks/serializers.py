from rest_framework import serializers
from django.contrib.auth import get_user_model


#Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only':True}
        } #never returns password in API responses

    #validate email uniqueness
    def validate_email(self, value):
        user = get_user_model()
        if user.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    #create new user
    def create(self, validated_data):
        email = validated_data["email"]
        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]

        user = get_user_model()
        new_user = user.objects.create(
            email=email, 
            username=username, 
            first_name=first_name, 
            last_name=last_name
        )

        new_user.set_password(password) #hash password properly
        new_user.save() #save user to database
        return new_user


#Serializer for user profile update
class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["bio", "profile_picture", "created_at", "updated_at"]