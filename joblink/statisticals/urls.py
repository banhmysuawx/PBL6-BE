from django.urls import path

from .views import TopCompany,TopJobCategory,TopJobHighSalary
urlpatterns = [
    path('statisticals/top-company', TopCompany.as_view()),
    path('statisticals/top-job-category', TopJobCategory.as_view()),
    path('statisticals/top-job-high-salary', TopJobHighSalary.as_view())
]
