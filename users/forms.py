from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Custom form for creating new users in the admin.
    Includes all relevant fields for your custom User model.
    """
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "role",
            "is_active",
            "is_staff",
        )


class CustomUserChangeForm(UserChangeForm):
    """
    Custom form for updating existing users in the admin.
    """
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "role",
            "is_active",
            "is_staff",
        )
