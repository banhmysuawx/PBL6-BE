from rest_framework import serializers

from accounts.models import User
from accounts.serializers import UserSerializer
from job.models import Job
from job.serializers import JobSerializer
from applications.models import Application
class ApplyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id'
        )

class ApplyJobSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    class Meta:
        model = Application
        fields = '__all__'
    def get_user(self, obj):
        return obj.user.id

class ApplicantSerializer(serializers.ModelSerializer):
    # user = ApplyUserSerializer(read_only = True , many =False)
    applied_user = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = ("id","user","job_id", "job", "status", "fullname", "email","cv","cover_letter","applied_user")
        # fields = '__all__'

    def get_status(self, obj):
        return obj.get_status

    def get_job(self, obj):
        return JobSerializer(obj.job).data

    def get_applied_user(self, obj):
        return ApplyJobSerializer(obj.user).data

class AppliedJobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    applicant = serializers.SerializerMethodField("_applicant")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Job
        fields = "__all__"

    def _applicant(self, obj):
        user = self.context.get("request", None).user
        # job = self.context.get("request", None).job
        return ApplicantSerializer(Application.objects.get(user=user, job=obj)).data