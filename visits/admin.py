# Register your models here.
from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pregnancy',
        'mother',
        'health_worker',
        'visit_date',
        'next_visit_date',
        'created_at',
    )
    list_filter = ('visit_date', 'health_worker')
    search_fields = (
        'mother__user__first_name',
        'mother__user__last_name',
        'health_worker__user__first_name',
        'health_worker__user__last_name',
    )
    ordering = ('-visit_date',)
