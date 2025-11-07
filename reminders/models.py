# Create your models here.
from django.db import models
from django.utils import timezone
from reminders.managers import ReminderManager

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    reminder_time = models.DateTimeField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Relationships (optional, you can extend later)
    # For example, link to pregnancy or visit
    pregnancy = models.ForeignKey('pregnancies.Pregnancy', on_delete=models.CASCADE, null=True, blank=True)
    visit = models.ForeignKey('visits.Visit', on_delete=models.CASCADE, null=True, blank=True)

    objects = ReminderManager()  # ✅ Attach our custom manager

    class Meta:
        ordering = ['-reminder_time']

    def __str__(self):
        return f"{self.title} — {'Sent' if self.sent else 'Pending'}"

    def is_due(self):
        """
        Returns True if this reminder is due to be sent.
        """
        return not self.sent and self.reminder_time <= timezone.now()
