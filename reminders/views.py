# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations and extra reminder actions.
    """
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Reminder.objects.all()

        return Reminder.objects.filter(
            reminder_time__gte=timezone.now() - timezone.timedelta(days=30)
        )

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'], url_path='due-soon')
    def due_soon(self, request):
        """
        Custom endpoint: return reminders due within the next 24 hours.
        """
        reminders = Reminder.objects.due_soon(days=1)
        serializer = self.get_serializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='overdue')
    def overdue(self, request):
        """
        Custom endpoint: return reminders that are overdue.
        """
        reminders = Reminder.objects.overdue()
        serializer = self.get_serializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
