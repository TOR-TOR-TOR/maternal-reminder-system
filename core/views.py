from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, permissions

class BaseModelViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    """
    Generic viewset for models inheriting from BaseModel.
    Provides CRUD + soft-delete support.
    """
    permission_classes = [permissions.IsAuthenticated]  # tweak as needed

    def perform_destroy(self, instance):
        # Soft-delete instead of actual delete
        instance.is_active = False
        instance.save()
