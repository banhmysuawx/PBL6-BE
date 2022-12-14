from django.db import models
from applicants.models.applicant_interview import ApplicantInterview

class PeriodTimeInterview(models.Model):
    applicant_interview = models.ForeignKey(ApplicantInterview,related_name="period_times",on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "period_time_interview"