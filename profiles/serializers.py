from rest_framework import serializers
from profiles.models import HealthWorkerProfile, MotherProfile
from users.models import User

# -------- Users --------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_active']  # adjust fields

# -------- Profiles --------
class HealthWorkerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested read-only user
    class Meta:
        model = HealthWorkerProfile
        fields = ['id', 'user', 'created_at', 'updated_at', 'is_active']

class MotherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = MotherProfile
        fields = ['id', 'user','created_at', 'updated_at', 'is_active']
