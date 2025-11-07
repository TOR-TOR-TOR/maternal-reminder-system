from rest_framework import serializers
from .models import Visit

class VisitSerializer(serializers.ModelSerializer):
    mother_name = serializers.CharField(source='mother.user.get_first_name', read_only=True)
    health_worker_name = serializers.CharField(source='health_worker.user.get_first_name', read_only=True)
    pregnancy_id = serializers.IntegerField(source='pregnancy.id', read_only=True)

    class Meta:
        model = Visit
        fields = [
            'id',
            'pregnancy_id',
            'mother_name',
            'health_worker_name',
            'visit_date',
            'blood_pressure',
            'weight',
            'notes',
            'next_visit_date',
            'created_at',
        ]
        read_only_fields = ['created_at']
