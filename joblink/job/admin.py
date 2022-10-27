from django.contrib import admin
from job.models.job import Job
from job.models.job_category import JobCategory
from job.models.job_location import JobLocation
from job.models.job_skill import JobSkill

# Register your models here.
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobLocation)
admin.site.register(JobSkill)