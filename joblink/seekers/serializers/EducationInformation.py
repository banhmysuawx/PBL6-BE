from rest_framework import serializers
from seekers.models import EducationInformation

class EducationInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationInformation
        fields = "__all__"