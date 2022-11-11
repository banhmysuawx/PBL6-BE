from django.db import models
from accounts.models import User
from job.models.job import Job

class STATUS_CHOICE(models.TextChoices):
    APPLY = "apply"
    TEST = "test"
    INTERVIEW = "interview"
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"

class Applicant(models.Model):
    candidate = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "applicants")
    job = models.ForeignKey(Job, on_delete= models.CASCADE, related_name = "applicants")
    status = models.CharField(max_length=20, choices = STATUS_CHOICE.choices, default = STATUS_CHOICE.APPLY)
    apply_date = models.DateTimeField(auto_now_add=True)
    status_do_test_date = models.DateTimeField(null=True, blank=True)
    status_interview_date = models.DateTimeField(null=True, blank=True)
    interview_date_official = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "applicants"