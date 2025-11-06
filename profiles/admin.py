from django.contrib import admin

# Register your models here.

from .models import MotherProfile, HealthWorkerProfile

@admin.register(MotherProfile)
class MotherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'address', 'emergency_contact')  # replace with actual fields
    search_fields = ('user__username', 'user__email')

@admin.register(HealthWorkerProfile)
class HealthWorkerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'facility_name', 'position')  # replace with actual fields
    search_fields = ('user__username', 'user__email')
