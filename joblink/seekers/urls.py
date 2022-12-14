from django.urls import path,include
from seekers.views.ExpirenceInformation import ExpirenceInformationView,ExpirenceInformationDetailView,ExpirenceInProfile
from seekers.views.SkillInformation import SkillInformationView,SkillInformationDetailView,SkillInProfile
from seekers.views.EducationInformation import EducationInformationView,EducationInformationDetailView, EducationInProfile
from seekers.views.SeekerProfile import SeekerProfileView,SeekerProfileDetailView,SeekerProfileCandidateView
from rest_framework import routers


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'profile-skill', SkillInProfile, basename='skill')
router.register(r'profile-expirence', ExpirenceInProfile, basename='expirence')
router.register(r'profile-education', EducationInProfile, basename='education')
router.register(r'candidate-profile', SeekerProfileCandidateView, basename='candidate-profile')


urlpatterns = [
    path('expirences', ExpirenceInformationView.as_view()),
    path('expirences/<int:pk>', ExpirenceInformationDetailView.as_view()),
    path('skills', SkillInformationView.as_view()),
    path('skills/<int:pk>', SkillInformationDetailView.as_view()),
    path('educations', EducationInformationView.as_view()),
    path('educations/<int:pk>', EducationInformationDetailView.as_view()),
    path('profile', SeekerProfileView.as_view()),
    path('profiles/<int:pk>', SeekerProfileDetailView.as_view()),
    path('',include(router.urls)),

]