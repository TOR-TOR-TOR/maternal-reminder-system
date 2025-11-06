# users/serializers/login_serializer.py
from rest_framework import serializers
from users.services.authentication_service import login_user 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        # Call your service to handle login logic
        user_data = login_user(email=email, password=password)
        return user_data
