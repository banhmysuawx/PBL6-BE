from django.db import models
from accounts.models import User

class SeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):
        return self.first_name+" "+self.last_name

    class Meta:
        db_table = "seekers_profile"
    

class EducationInformation(models.Model):
    seeker = models.ForeignKey(SeekerProfile,related_name="educations_information",on_delete=models.CASCADE)
    certificate_degree_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255, null=True, blank=True)
    starting_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    gpa = models.FloatField(null=True,blank=True,default=0.0)

    def __str__(self):
        return self.certificate_degree_name

    class Meta:
        db_table = "educations_information"
        ordering = ["completion_date"]

class ExpirenceInformation(models.Model):
    seeker = models.ForeignKey(SeekerProfile,related_name="expirences_information",on_delete=models.CASCADE)
    is_current_job = models.BooleanField(default=False)
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    job_location =  models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.job_title

    class Meta:
        db_table = "expirences_information"
        ordering = ["end_date"]

class SkillInformation(models.Model):
    seeker = models.ForeignKey(SeekerProfile,related_name="skills_information",on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    skill_level =  models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name

    class Meta:
        db_table = "skills_information"
        
