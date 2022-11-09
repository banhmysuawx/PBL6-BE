from accounts.models import User
from accounts.serializers import UserSerializer
from applications.models import Application
from job.models import Job
from job.serializers import JobSerializer
from rest_framework import serializers


class ApplyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "id"


class ApplyJobSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    id = serializers.IntegerField(read_only=True, required=False)
    cv = serializers.FileField(required=False, allow_null=True, default=None)

    class Meta:
        model = Application
        fields = "__all__"

    def create(self, validated_data):
        data = {
            "user": validated_data["user"],
            "job": validated_data["job"],
            "fullname": validated_data["fullname"],
            "email": validated_data["user"].email,
            "cv": validated_data["cv"],
            "cover_letter": validated_data["cover_letter"],
            "status": validated_data["status"],
            "test_result": validated_data["test_result"],
        }
        id_application = Application.objects.create(**data)
        validated_data["id"] = id_application.id
        return validated_data


class ApplicantSerializer(serializers.ModelSerializer):
    # user = ApplyUserSerializer(read_only = True , many =False)
    applied_user = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = (
            "id",
            "user",
            "job_id",
            "job",
            "status",
            "fullname",
            "email",
            "cv",
            "cover_letter",
            "applied_user",
        )
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
