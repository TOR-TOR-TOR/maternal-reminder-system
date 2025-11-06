from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "first_name", "middle_name", "last_name" ,"phone_number", "role", "is_staff", "is_active")
    list_filter = ("role", "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "middle_name", "last_name" , "phone_number", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email","first_name", "middle_name", "last_name", "phone_number", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email", "first_name", "middle_name", "last_name" , "phone_number")
    ordering = ("email",)


#admin.site.register(User) 
