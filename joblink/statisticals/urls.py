from django.urls import path

from .views import *
urlpatterns = [
    path('statisticals/top-company', TopCompany.as_view()),
    path('statisticals/top-job-category', TopJobCategory.as_view()),
    path('statisticals/top-job-high-salary', TopJobHighSalary.as_view()),
    path('statisticals/seeker-employer-by-month', SeekerAndEmployerByMonth.as_view())
]
