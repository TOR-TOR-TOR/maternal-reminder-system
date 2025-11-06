# users/services/authentication_service.py

from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()

# 🔹 Registration logic
def register_user(email, password, first_name=None, last_name=None):
    # Check if user already exists
    if User.objects.filter(email=email).exists():
        raise AuthenticationFailed("A user with this email already exists.")

    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    # Generate JWT tokens
    #Returns JWT tokens right away (instant login after registration)
    refresh = RefreshToken.for_user(user)
    return {
        "message": "User registered successfully.",
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    }


# 🔹 Login logic
def login_user(email, password):
    user = authenticate(email=email, password=password)

    if user is None:
        raise AuthenticationFailed("Invalid email or password.")

#Generates new JWT tokens if valid
    refresh = RefreshToken.for_user(user)
    return {
        "message": "Login successful.",
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user": {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    }
