from django.contrib import admin
from applicants.models.applicant import Applicant
from applicants.models.applicant_test import ApplicantTest
from applicants.models.applicant_interview import ApplicantInterview
from applicants.models.period_time_interview import PeriodTimeInterview
# Register your models here.

admin.site.register(Applicant)
admin.site.register(ApplicantTest)
admin.site.register(ApplicantInterview)
admin.site.register(PeriodTimeInterview)

