from django.urls import path,include
from applicants.views.applicant import ApplicantView,ApplicantCompanyView,ApplicantDetaiView
from rest_framework import routers


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'company', ApplicantCompanyView, basename='applicant-company')

urlpatterns = [
    path('applicant', ApplicantView.as_view()),
    path('applicant/<int:pk>', ApplicantDetaiView.as_view()),
    path('',include(router.urls)),

]
