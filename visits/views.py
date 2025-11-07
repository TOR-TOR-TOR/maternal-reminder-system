# Create your views here.
from rest_framework import viewsets, permissions

from pregnancies import serializers
from .models import Visit
from .serializers import VisitSerializer
from pregnancies.serializers import  PregnancySerializer
from profiles.models import HealthWorkerProfile, MotherProfile
from pregnancies.models import Pregnancy

class VisitViewSet(viewsets.ModelViewSet):
    serializer_class = VisitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        # Health workers see visits they handled
        if hasattr(user, 'health_worker_profile'):
            return Visit.objects.for_health_worker(user.health_worker_profile)
        
        # Mothers see only their own visits
        elif hasattr(user, 'mother_profile'):
            return Visit.objects.for_mother(user.mother_profile)
        
        # Admins see everything
        return Visit.objects.all()

    def perform_create(self, serializer):
        user = self.request.user

        # Auto-link logged-in health worker
        if hasattr(user, 'health_worker_profile'):
            health_worker = user.health_worker_profile
            pregnancy_id = self.request.data.get('pregnancy')

            try:
                pregnancy = Pregnancy.objects.get(id=pregnancy_id)
            except Pregnancy.DoesNotExist:
                raise serializers.ValidationError({'pregnancy': 'Invalid pregnancy ID'})

            serializer.save(
                health_worker=health_worker,
                mother=pregnancy.mother,
                pregnancy=pregnancy
            )

        else:
            raise permissions.PermissionDenied("Only health workers can create visits.")
