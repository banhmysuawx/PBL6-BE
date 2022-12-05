from rest_framework import serializers
from applicants.models.period_time_interview import PeriodTimeInterview

class PeriodTimeInterviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PeriodTimeInterview
        fields = "__all__"

