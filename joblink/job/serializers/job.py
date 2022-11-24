from rest_framework import serializers
from job.models.job import Job
from companies.serializers import CompanySerializer
from job.serializers.job_location import JobLocationSerializer
from job.serializers.job_skill import JobSkillSerializer

class JobSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)

    class Meta:
        model = Job
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        locations_data = [item.location_name for item in instance.locations.all()]
        ret['locations_name']=locations_data
        ret['category_name'] = instance.category.name
        return ret