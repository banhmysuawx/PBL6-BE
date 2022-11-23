from rest_framework import serializers
from job.models.job_category import JobCategory
from job.serializers.job import JobSerializer

class JobCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobCategory
        fields = "__all__"

class getJobCategorySerializer(serializers.Serializer):
    category = JobCategorySerializer()
    jobs = JobSerializer(many=True)
