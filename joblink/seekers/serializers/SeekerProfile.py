from rest_framework import serializers
from seekers.models import SeekerProfile

class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = "__all__"