from django.urls import path,include
from job.views.job_category import JobCategoryView,JobCategoryDetailView
from job.views.job_location import JobLocationView,JobLocationDetailView
from job.views.job_skill import JobSkillView,JobSkillDetailView
from job.views.job import JobView,JobDetailView,SumJobView
from job.views.job_category import CategoryJobInCompany
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'company', CategoryJobInCompany)



urlpatterns = [
    path('categories', JobCategoryView.as_view()),
    path('categories/<int:pk>', JobCategoryDetailView.as_view()),
    path('locations', JobLocationView.as_view()),
    path('locations/<int:pk>', JobLocationDetailView.as_view()),
    path('skills', JobSkillView.as_view()),
    path('skills/<int:pk>', JobSkillDetailView.as_view()),
    path('jobs', JobView.as_view()),
    path('jobs/<int:pk>', JobDetailView.as_view()),
    path('jobs/sum_jobs', SumJobView.as_view()),
    path('',include(router.urls)),

]
