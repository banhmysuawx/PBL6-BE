from rest_framework import serializers
from seekers.models import SkillInformation

class SkillInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillInformation
        fields = "__all__"