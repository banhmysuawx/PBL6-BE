from rest_framework import serializers
from seekers.models import ExpirenceInformation

class ExpirenceInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpirenceInformation
        fields = "__all__"