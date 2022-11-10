from django import db
from django.db import models
from companies.models import Company

class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name="job_categories",null=True)

    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "job_categories"