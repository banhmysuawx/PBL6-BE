from operator import mod
import black
from django.db import models
from companies.models import Company

class JobLocation(models.Model):
    location_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100, null = True, blank = True)
    city = models.CharField(max_length =100, null= True, blank=True)
    state = models.CharField(max_length=100, null = True, blank = True)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100, null = True, blank = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name= "job_locations",null=True)

    class Meta:
        db_table = "job_locations"
