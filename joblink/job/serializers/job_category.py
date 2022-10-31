from rest_framework import serializers
from job.models.job_category import JobCategory

class JobCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobCategory
        fields = "__all__"