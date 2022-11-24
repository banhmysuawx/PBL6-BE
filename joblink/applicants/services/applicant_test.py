from applicants.models.applicant_test import ApplicantTest
from applicants.models.applicant import Applicant
from datetime import datetime,timedelta
from django.utils import timezone

class ApplicantTestService():

    @classmethod
    def create_applicant_test(self,id_applicant):
        applicant = Applicant.objects.get(pk=id_applicant)
        job = applicant.job
        date_expired = datetime.now(tz=timezone.utc) + timedelta(days=job.limited_day_do_test)
        try:
            ApplicantTest.objects.create(applicant=applicant,date_expired_at=date_expired)
        except Exception:
            raise Exception
