# profiles are automatically created when user registers

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from profiles.models import MotherProfile, HealthWorkerProfile, AdminProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_role_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'mother':
            MotherProfile.objects.create(user=instance)
        elif instance.role == 'health_worker':
            HealthWorkerProfile.objects.create(user=instance)
        elif instance.role == 'admin':
            AdminProfile.objects.create(user=instance)
