from django.urls import path,include
from job.views.job_category import JobCategoryView,JobCategoryDetailView
from job.views.job_location import JobLocationView,JobLocationDetailView
from job.views.job_skill import JobSkillView,JobSkillDetailView
from job.views.job import JobView,JobDetailView,SumJobView,JobInCompanyView,JobListAdminView,JobDetailAdminView,JobInUserView
from job.views.job_category import CategoryJobInCompany
from job.views.job_location import JobLocationInCompanyView
from job.views.job_skill import JobSkillInCompanyView
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'company', CategoryJobInCompany, basename='category-company')
router.register(r'company',JobLocationInCompanyView, basename='job-company')
router.register(r'company',JobSkillInCompanyView, basename='skill-company')
router.register(r'company',JobInCompanyView, basename='job-company')
router.register(r'user',JobInUserView, basename='job-user')

urlpatterns = [
    path('categories', JobCategoryView.as_view(), name="category"),
    path('categories/<int:pk>', JobCategoryDetailView.as_view()),
    path('locations', JobLocationView.as_view(), name="location"),
    path('locations/<int:pk>', JobLocationDetailView.as_view()),
    path('skills', JobSkillView.as_view(), name="skill"),
    path('skills/<int:pk>', JobSkillDetailView.as_view()),
    path('jobs', JobView.as_view(), name="job"),
    path('jobs/<int:pk>', JobDetailView.as_view()),
    path('jobs-list/admin', JobListAdminView.as_view()),
    path('jobs-detail/admin', JobDetailAdminView.as_view()),
    path('jobs/sum_jobs', SumJobView.as_view()),
    path('',include(router.urls)),
]
