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

class ApplicantInterviewEventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    start = serializers.DateTimeField("%Y-%m-%d %H:%M")
    end = serializers.DateTimeField("%Y-%m-%d %H:%M")