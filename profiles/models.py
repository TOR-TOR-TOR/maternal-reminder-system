from django.db import models

# Create your models here.

from django.conf import settings
from core.models import BaseModel

class MotherProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mother_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    emergency_contact = models.CharField(max_length=20, blank=True)
    # medical_history = models.TextField(blank=True)
    #expected_delivery_date = models.DateField(null=True, blank=True)
    #profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"Mother: {self.user.first_name} {self.user.last_name}"

class HealthWorkerProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='health_worker_profile')
    facility_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    # experience_years = models.PositiveIntegerField(default=0)
    assigned_mothers = models.ManyToManyField(MotherProfile, blank=True, related_name="health_workers")
    # profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"Health Worker: {self.user.first_name} ({self.facility_name})"
    
class AdminProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, blank=True)
    access_level = models.CharField(max_length=50, default="super")

    def __str__(self):
        return f"Admin: {self.user.email}"