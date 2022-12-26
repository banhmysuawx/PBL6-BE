from django.db import models
from accounts.models import User
from job.models.job import Job

class STATUS_CHOICE(models.TextChoices):
    APPLY = "apply"
    TEST = "test"
    SET_SCHEDULE = "set_schedule"
    INTERVIEW_PENDING = "interview_pending"
    SCHEDULE_INTERVIEW = "schedule_interview"
    CANCEL_INTERVIEW = "cancel_interview"
    INTERVIEW_COMPLETE = "interview_complete"
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"

def name_file(instance, filename):
    return "cv/"+"/".join([str(instance.candidate.id), filename])

class Applicant(models.Model):
    candidate = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "applicants")
    job = models.ForeignKey(Job, on_delete= models.CASCADE, related_name = "applicants")
    status = models.CharField(max_length=20, choices = STATUS_CHOICE.choices, default = STATUS_CHOICE.APPLY)
    apply_date = models.DateTimeField(auto_now_add=True)
    status_do_test_date = models.DateTimeField(null=True, blank=True)
    status_interview_date = models.DateTimeField(null=True, blank=True)
    interview_date_official = models.DateTimeField(null=True,blank=True)
    cv = models.FileField(null=True,blank=True, upload_to=name_file)
    information_added =models.TextField(blank=True,null=True)
    is_send_email = models.BooleanField(default=False, null=True,blank=True)
    link_gg_meet = models.URLField(max_length = 200, null=True, blank=True)

    class Meta:
        db_table = "applicants"