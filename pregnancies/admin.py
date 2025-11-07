from django.contrib import admin

# Register your models here.
from .models import Pregnancy

@admin.register(Pregnancy)
class PregnancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'mother', 'expected_due_date', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('mother__user__first_name', 'mother__user__last_name')
    ordering = ('-created_at',)