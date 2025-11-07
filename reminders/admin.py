# Register your models here.
from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'reminder_date', 'is_sent')
    list_filter = ('is_sent', 'reminder_date')
    search_fields = ('message', 'user__email', 'user__first_name')
    ordering = ('reminder_date',)
