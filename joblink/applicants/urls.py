from django.urls import path
from applicants.views.applicant import ApplicantView

urlpatterns = [
    path('applicant', ApplicantView.as_view()),
   
]
