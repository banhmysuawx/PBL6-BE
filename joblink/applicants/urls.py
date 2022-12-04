from django.urls import path,include
from applicants.views.applicant import ApplicantView,ApplicantCompanyView,ApplicantDetaiView,ApplicantCandidateView, SaveResultView
from applicants.views.applicant_interview import ApplicantInterviewView,GetApplicantInterviewView,ApplicantInterviewDetailView
from applicants.views.period_time_interview import PeriodTimeByInterview
from rest_framework import routers


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'company', ApplicantCompanyView, basename='applicant-company')
router.register(r'candidate', ApplicantCandidateView, basename='applicant-candidate')
router.register(r'company/applicant-interview', GetApplicantInterviewView, basename='applicant-interview')
router.register(r'company/period-interview', PeriodTimeByInterview, basename='period-interview')
# router.register(r'company/save-result', SaveResultView, basename='save-result')


urlpatterns = [
    path('applicant', ApplicantView.as_view()),
    path('applicant/<int:pk>', ApplicantDetaiView.as_view()),
    path('applicant-interview', ApplicantInterviewView.as_view()),
    path('applicant-interview/<int:pk>', ApplicantInterviewDetailView.as_view()),
    path('',include(router.urls)),

]
