"""Provides reusable class mixins for models and views."""
"""
core/mixins.py
Reusable mixins that add shared behavior to views or models across the project.
Keeps the code DRY (Don't Repeat Yourself) and readable.
"""

from rest_framework import mixins, generics, status
from rest_framework.response import Response
from core.utils import soft_delete


class SoftDeleteMixin:
    """
    A mixin that adds soft-delete behavior to Django model views.
    Instead of deleting from the database, it marks `is_active=False`.
    """

    def perform_destroy(self, instance):
        soft_delete(instance)


class ActiveOnlyQuerySetMixin:
    """
    Filters queryset to only include active records by default.
    Useful for models using `is_active` from BaseModel.
    """

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_active=True)


class CreatedUpdatedMixin:
    """
    Automatically sets `created_by` and `updated_by` fields on save.
    Add this if your model tracks who created/updated it.
    """

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class StandardResponseMixin:
    """
    Adds a consistent API response format for list/retrieve/create actions.
    Makes frontend integration predictable and debugging easier.
    """

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Created successfully", "data": response.data},
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Updated successfully", "data": response.data},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
