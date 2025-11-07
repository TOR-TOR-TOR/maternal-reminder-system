# Create your views here.
from rest_framework import viewsets, permissions
from .models import Pregnancy
from .serializers import PregnancySerializer
from profiles.models import MotherProfile
from core.permissions import IsHealthWorkerOrAdmin
from rest_framework import filters

class PregnancyViewSet(viewsets.ModelViewSet):
    serializer_class = PregnancySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['mother__user__full_name']
    ordering_fields = ['expected_due_date', 'created_at']

    def get_queryset(self):
        user = self.request.user

        # If user is a mother → show only her pregnancies
        if hasattr(user, 'mother_profile'):
            return Pregnancy.objects.for_mother(user.mother_profile)

        # If user is a health worker → show all pregnancies (or later filter by assigned mothers)
        if hasattr(user, 'health_worker_profile'):
            return Pregnancy.objects.all()  # we’ll refine this later for assigned patients

        # If admin or staff → show everything
        if user.is_staff:
            return Pregnancy.objects.all()

        # Default empty queryset (safety fallback)
        return Pregnancy.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        # Since the permission class already filters creation rights, this is safe
        serializer.save()