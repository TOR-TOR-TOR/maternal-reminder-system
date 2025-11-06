"""Utility functions and helpers that can be used throughout the project."""
"""
core/utils.py
Reusable helper functions used across the project.
Focus: time, IDs, status handling, and small utilities that simplify logic.
"""

import uuid
from datetime import datetime, timedelta, timezone
from django.utils import timezone as dj_timezone
from core.constants import DEFAULT_REMINDER_OFFSET_HOURS, DEFAULT_TIMEZONE


def generate_unique_code(prefix: str = "", length: int = 8) -> str:
    """
    Generates a unique code for identifiers like appointments, reminders, or users.
    """
    unique = uuid.uuid4().hex[:length].upper()
    return f"{prefix}{unique}" if prefix else unique


def get_default_reminder_time(appointment_datetime: datetime) -> datetime:
    """
    Calculates when a reminder should be sent before the appointment.
    Uses DEFAULT_REMINDER_OFFSET_HOURS from constants.
    """
    reminder_time = appointment_datetime - timedelta(hours=DEFAULT_REMINDER_OFFSET_HOURS)
    return reminder_time


def now_local():
    """
    Returns the current datetime adjusted to DEFAULT_TIMEZONE.
    (You can later hook in pytz or zoneinfo for exact localization.)
    """
    return dj_timezone.now()


def humanize_time_diff(past_time: datetime) -> str:
    """
    Returns a human-friendly string for time differences.
    Example: '3 hours ago', '2 days ago'.
    """
    diff = dj_timezone.now() - past_time
    seconds = diff.total_seconds()

    if seconds < 60:
        return f"{int(seconds)}s ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)}h ago"
    else:
        return f"{int(seconds // 86400)}d ago"


def soft_delete(instance):
    """
    Soft-delete a model instance by toggling its is_active flag instead of removing it.
    """
    instance.is_active = False
    instance.save()
    return instance
