from rest_framework import serializers
from applicants.models.applicant_interview import ApplicantInterview

class ApplicantInterviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ApplicantInterview
        fields = "__all__"

class PeriodTimeSerializer(serializers.Serializer):
    start = serializers.DateTimeField(format="%H:%M")
    end = serializers.DateTimeField(format="%H:%M")

class ListPeriodTimeSerializer(serializers.Serializer):
    day = serializers.DateField()
    available = PeriodTimeSerializer(many = True)