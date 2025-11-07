from django.utils import timezone
from .models import Reminder

def send_due_reminders():
    now = timezone.now()
    upcoming = Reminder.objects.due_soon(days=1)

    """  
    for reminder in upcoming:
        # Simulate sending (later we can hook to email/SMS)
        print(f"📢 Reminder for {reminder.message} — due on {reminder.remind_at}")
  """  
    for reminder in upcoming:
        # This simulates sending an alert (can later be SMS/email)
        print(f"📢 Reminder for {reminder.message} — due on {reminder.remind_at}")

    print(f"✅ {len(upcoming)} reminders processed at {now}.")
