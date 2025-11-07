from rest_framework import serializers
from .models import Pregnancy

class PregnancySerializer(serializers.ModelSerializer):
    mother_name = serializers.CharField(source='mother.user.get_first_name', read_only=True)
    mother_id = serializers.IntegerField(source='mother.id', read_only=True)

    class Meta:
        model = Pregnancy
        fields = [
            'id',
            'mother_id',
            'mother_name',
            'expected_due_date',
            'last_checkup_date',
            'notes',
            'is_active',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'mother_id', 'mother_name']


# auto-linking the logged-in mother
class PregnancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregnancy
        fields = ['expected_due_date', 'last_checkup_date', 'notes']
