from rest_framework import serializers
from job.models.job import Job
from companies.serializers import CompanySerializer
from job.serializers.job_location import JobLocationSerializer
from job.serializers.job_skill import JobSkillSerializer

class JobSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d")
    company = CompanySerializer()
    locations = JobLocationSerializer(many=True) 
    skills = JobSkillSerializer(many=True)

    class Meta:
        model = Job
        fields = "__all__"