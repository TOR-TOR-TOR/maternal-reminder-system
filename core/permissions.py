"""Holds reusable permission classes for role-based access control."""
"""
core/permissions.py
Centralized permission logic for role-based access control (RBAC).
Used across the project to check if a user can perform specific actions.
"""

from rest_framework.permissions import BasePermission
from core.constants import USER_ROLES
from rest_framework import permissions

class IsMother(BasePermission):
    """Allows access only to users with the 'mother' role."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "mother")


class IsHealthWorker(BasePermission):
    """Allows access only to users with the 'health_worker' role."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "health_worker")


class IsAdmin(BasePermission):
    """Allows access only to users with the 'admin' role."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "admin")


class IsDataClerk(BasePermission):
    """Allows access only to users with the 'data_clerk' role."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == "data_clerk")


class IsActiveUser(BasePermission):
    """Grants access only to users marked as active in the system."""
    def has_permission(self, request, view):
        return bool(request.user and getattr(request.user, "is_active", False))


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners can edit their data.
    Read-only allowed for others if needed.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for the object's owner
        return obj == request.user