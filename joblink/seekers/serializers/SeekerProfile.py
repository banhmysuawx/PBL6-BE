from rest_framework import serializers
from seekers.models import SeekerProfile
from seekers.serializers.EducationInformation import EducationInformationSerializer
from seekers.serializers.SkillInformation import SkillInformationSerializer
from seekers.serializers.ExpirenceInformation import ExpirenceInformationSerializer
from accounts.serializers import UserSerializer


class SeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = "__all__"

class SeekerDetailSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    seeker = SeekerProfileSerializer(read_only=True)
    skills = SkillInformationSerializer(many=True, read_only=True)
    educations = EducationInformationSerializer(many=True, read_only=True)
    expirences = ExpirenceInformationSerializer(many=True, read_only= True)
            


