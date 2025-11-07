from django.db import models
from django.utils import timezone
from datetime import timedelta

class ReminderManager(models.Manager):
    def due_soon(self, days=1):
        """
        Get reminders that are due within the next `days`.
        """
        now = timezone.now()
        upcoming = now + timedelta(days=days)
        return self.filter(reminder_time__lte=upcoming, sent=False)

    def overdue(self):
        """
        Get reminders that were supposed to be sent but weren't.
        """
        now = timezone.now()
        return self.filter(reminder_time__lt=now, sent=False)

    def sent(self):
        """
        Get reminders that have already been sent.
        """
        return self.filter(sent=True)
