from django.db import models
from django.utils import timezone

class PregnancyManager(models.Manager):
    def active(self):
        """Return only ongoing pregnancies"""
        return self.filter(is_active=True)
    
    def completed(self):
        """Return pregnancies marked as completed"""
        return self.filter(is_active=False)
    
    def for_mother(self, mother):
        """Get all pregnancies for a specific mother"""
        return self.filter(mother=mother)
    
    def due_soon(self):
        """Pregnancies due within the next 7 days"""
        today = timezone.now().date()
        return self.filter(expected_due_date__range=[today, today + timezone.timedelta(days=7)])
