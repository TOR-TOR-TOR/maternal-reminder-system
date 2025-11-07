from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings
from pregnancies.models import Pregnancy
from profiles.models import MotherProfile, HealthWorkerProfile
from .managers import VisitManager

class Visit(models.Model):
    pregnancy = models.ForeignKey(
        Pregnancy, 
        on_delete=models.CASCADE, 
        related_name='visits'
    )
    mother = models.ForeignKey(
        MotherProfile, 
        on_delete=models.CASCADE, 
        related_name='visits'
    )
    health_worker = models.ForeignKey(
        HealthWorkerProfile, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='handled_visits'
    )

    visit_date = models.DateField(default=timezone.now)
    blood_pressure = models.CharField(max_length=50, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    next_visit_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = VisitManager()

    class Meta:
        ordering = ['-visit_date']
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'

    def __str__(self):
        return f"Visit on {self.visit_date} for {self.mother.user.get_first_name()}"
