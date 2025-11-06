"""Contains all shared constants, choices, and enums used across the system."""
"""
core/constants.py
Shared enums, choices, and system-wide constants used across the project.
Edit carefully — changing these affects DB choices and business logic.
"""

# User role choices (single source of truth)
USER_ROLES = (
    ("mother", "Mother"),
    ("health_worker", "Health Worker"),
    ("admin", "Admin"),
   
)

# Appointment status choices
APPOINTMENT_STATUS = (
    ("pending", "Pending"),
    ("confirmed", "Confirmed"),
    ("completed", "Completed"),
    ("missed", "Missed"),
    ("cancelled", "Cancelled"),
)

# Reminder delivery status
REMINDER_STATUS = (
    ("queued", "Queued"),
    ("sent", "Sent"),
    ("failed", "Failed"),
    ("delivered", "Delivered"),
)

# Common time windows or defaults
DEFAULT_REMINDER_OFFSET_HOURS = 24  # default: send reminder 24 hours before appointment
DEFAULT_TIMEZONE = "Africa/Nairobi"

# Message/template keys (used by message templating engine)
TEMPLATE_KEYS = {
    "appointment_reminder": "appointment_reminder",
    "followup_reminder": "followup_reminder",
    "general_broadcast": "general_broadcast"
}

# Pagination / limits
DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100

# Feature flags (toggleable booleans that can be used later)
FEATURE_FLAGS = {
    "ENABLE_TWO_WAY_SMS": False,
    "ENABLE_PILOT_ANALYTICS": True,
}
