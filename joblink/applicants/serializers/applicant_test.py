from rest_framework import serializers
from applicants.models.applicant_test import ApplicantTest

class ApplicantSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ApplicantTest
        fields = "__all__"