from rest_framework import serializers
from job.models.job import Job
from job.serializers.job_location import JobLocationSerializer
from job.serializers.job_skill import JobSkillSerializer
from companies.serializers import CompanySerializer
from companies.serializers import CompanySerializer
from comment_posts.serializers import CommentPostSerializer
from applicants.models.applicant import Applicant

class JobSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)

    class Meta:
        model = Job
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        locations_data = [item.location_name for item in instance.locations.all()]
        list_status= ['apply','test','set_schedule','interview_pending','schedule_interview','interview_complete']
        number = Applicant.objects.filter(job_id=instance.id, status__in = list_status).count()
        ret['locations_name']=locations_data
        ret['category_name'] = instance.category.name
        ret['number_apply'] = number
        return ret

class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    created_at = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    skills = JobSkillSerializer(many=True)
    locations = JobLocationSerializer(many=True)

    class Meta:
        model = Job
        fields = "__all__"


class JobUserSerializer(serializers.Serializer):
    job = JobDetailSerializer()
    comments = CommentPostSerializer(many=True)


