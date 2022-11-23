from django.db import models
from applicants.models.applicant import Applicant

class ApplicantTest(models.Model):

    applicant = models.OneToOneField(Applicant, on_delete = models.CASCADE)
    start_date = models.DateTimeField(null=True,blank=True)
    finish_date =  models.DateTimeField(null=True,blank=True)
    date_expired_at =  models.DateTimeField(null=True,blank=True)
    result = models.FloatField(default=0)

    class Meta:
        db_table = "applicant_test"