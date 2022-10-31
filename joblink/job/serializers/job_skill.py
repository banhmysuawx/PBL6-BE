from rest_framework import serializers
from job.models.job_skill import JobSkill

class JobSkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobSkill
        fields = "__all__"