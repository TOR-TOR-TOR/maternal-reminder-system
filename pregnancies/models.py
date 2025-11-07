from django.db import models

# Create your models here.
from django.db import models
from profiles.models import MotherProfile
from .managers import PregnancyManager

class Pregnancy(models.Model):
    mother = models.ForeignKey(MotherProfile, on_delete=models.CASCADE, related_name='pregnancies')
    expected_due_date = models.DateField()
    last_checkup_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PregnancyManager()  # custom manager

    def __str__(self):
        return f"{self.mother.user.get_first_name()} - Due {self.expected_due_date}"

    class Meta:
        ordering = ['-created_at']
