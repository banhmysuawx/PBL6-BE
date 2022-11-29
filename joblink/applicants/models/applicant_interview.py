from django.db import models
from applicants.models.applicant import Applicant

class CHOICE_SET_SCHEDULE(models.TextChoices):
    AUTOMATE = "automate"
    MANUAL = "manual"


class ApplicantInterview(models.Model):
    applicant = models.OneToOneField(Applicant,on_delete=models.CASCADE)
    start_interview = models.DateTimeField(null=True,blank=True)
    end_interview =  models.DateTimeField(null=True,blank=True)
    active = models.BooleanField(default=True)
    end_set_schedule_interview = models.DateField(null=True, blank=True)
    choice_set_schedule_interview = models.CharField(max_length=20, choices=CHOICE_SET_SCHEDULE.choices, default=CHOICE_SET_SCHEDULE.AUTOMATE)
    

    class Meta:
        db_table = "applicant_interview"
    
