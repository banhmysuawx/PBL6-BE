from django.urls import path,include
from seekers.views.ExpirenceInformation import ExpirenceInformationView,ExpirenceInformationDetailView
from seekers.views.SkillInformation import SkillInformationView,SkillInformationDetailView
from seekers.views.EducationInformation import EducationInformationView,EducationInformationDetailView
from seekers.views.SeekerProfile import SeekerProfileView,SeekerProfileDetailView

urlpatterns = [
    path('expirences', ExpirenceInformationView.as_view()),
    path('expirences/<int:pk>', ExpirenceInformationDetailView.as_view()),
    path('skills', SkillInformationView.as_view()),
    path('skills/<int:pk>', SkillInformationDetailView.as_view()),
    path('educations', EducationInformationView.as_view()),
    path('educations/<int:pk>', EducationInformationDetailView.as_view()),
    path('profile', SeekerProfileView.as_view()),
    path('profiles/<int:pk>', SeekerProfileDetailView.as_view()),

]