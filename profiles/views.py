from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from profiles.models import MotherProfile, HealthWorkerProfile
from profiles.serializers import MotherProfileSerializer, HealthWorkerProfileSerializer

class MotherProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for MotherProfile.
    Only returns profiles linked to the logged-in user.
    """
    serializer_class = MotherProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'motherprofile'):
            return MotherProfile.objects.filter(user=user)
        return MotherProfile.objects.none()


class HealthWorkerProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for HealthWorkerProfile.
    Only returns profiles linked to the logged-in user.
    """
    serializer_class = HealthWorkerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'healthworkerprofile'):
            return HealthWorkerProfile.objects.filter(user=user)
        return HealthWorkerProfile.objects.none()
