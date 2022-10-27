from rest_framework import serializers
from job.models.job_location import JobLocation

class JobLocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobLocation
        fields = "__all__"