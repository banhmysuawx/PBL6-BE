from django.contrib import admin
from applicants.models.applicant import Applicant
from applicants.models.applicant_test import ApplicantTest
# Register your models here.

admin.site.register(Applicant)
admin.site.register(ApplicantTest)
