from rest_framework import serializers
from applicants.models.applicant import Applicant
from job.serializers.job import JobSerializer
from accounts.serializers import UserSerializer

class ApplicantSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    candidate = UserSerializer()

    class Meta:
        model = Applicant
        fields = "__all__"