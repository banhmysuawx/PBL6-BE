from typing import OrderedDict
from django.db import models
from accounts.models import User
from joblink import settings

# Create your models here.
class Company(models.Model):
    """Company model"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL , limit_choices_to = {
            'is_staff':True}, on_delete = models.CASCADE)
    profile_description = models.TextField(max_length = 256 , blank=True , default='')
    established_date =  models.DateTimeField(auto_now_add=True)
    image = models.TextField(max_length = 256 , blank=True , default='')
    company_name = models.CharField(max_length= 256, blank=True , default='')
    company_location = models.CharField(max_length = 256 , blank=True , default='')

    def __str__(self):
        return self.company_name