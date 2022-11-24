from rest_framework import serializers
from applicants.models.applicant import Applicant
from applicants.models.applicant_test import ApplicantTest
from seekers.models import SeekerProfile

class ApplicantSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Applicant
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        try:
            data = SeekerProfile.objects.get(user_id=instance.candidate.id)
            ret['candidate_name']= data.fullname
            ret['seeker_id'] = data.id
            ret['apply_format_day'] = instance.apply_date.strftime("%Y-%m-%d") 
            if (instance.status_do_test_date != ''):
                ret['test_format_day'] = instance.status_do_test_date.strftime("%Y-%m-%d") 
                applicant_test = ApplicantTest.objects.get(applicant_id=instance.id)
                ret['expired_format_day'] = applicant_test.date_expired_at.strftime("%Y-%m-%d") 
                ret['result_test'] = applicant_test.result
        except Exception:
            print("err")
        return ret