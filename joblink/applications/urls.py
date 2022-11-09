from django.urls import path
from .views import ApplyJobApiView,AppliedJobsAPIView

urlpatterns = [
    path('employee/apply/<int:job_id>/', ApplyJobApiView.as_view()),
    path("employee/applied/", AppliedJobsAPIView.as_view()),
]