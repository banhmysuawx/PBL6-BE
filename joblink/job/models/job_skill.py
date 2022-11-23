from companies.models import Company
from django.db import models

class JobSkill(models.Model):
    name = models.CharField(max_length = 100)
    level_name = models.CharField(max_length= 100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name ="job_skills",null=True )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "job_skills"


