from django.db import models
from job.models.job_category import JobCategory
from job.models.job_location import JobLocation
from job.models.job_skill import JobSkill
from companies.models import Company

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(JobCategory, on_delete = models.CASCADE, related_name="jobs") 
    is_active = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    salary = models.CharField(max_length = 100, null= True, blank= True)
    locations = models.ManyToManyField(JobLocation, related_name="jobs")
    is_company_name_hidden = models.BooleanField(default=True)
    skills = models.ManyToManyField(JobSkill, related_name="jobs")
    company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name="jobs",null=True)

    class Meta:
        db_table = "jobs"


