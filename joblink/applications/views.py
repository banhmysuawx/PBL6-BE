from applications.models import Application
from applications.serializers import (
    ApplicantSerializer,
    AppliedJobSerializer,
    ApplyJobSerializer,
)
from job.models import Job
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

# Create your views here.
from django.shortcuts import render


class ApplyJobApiView(CreateAPIView):
    serializer_class = ApplyJobSerializer
    # permission_classes = [
    #     IsAuthenticatedOrReadOnly,
    # ]
    def post(self, request, *args, **kwargs):
        request.data["job"] = kwargs["job_id"]
        if request.user.is_authenticated:
            request.data["user"] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance_id = serializer.save()["id"]
        serializer = ApplyJobSerializer(Application.objects.get(id=instance_id))
        # Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AppliedJobsAPIView(ListAPIView):
    serializer_class = AppliedJobSerializer
    # permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        applied_jobs_id = list(Application.objects.filter(user_id=user.id).values_list("job_id", flat=True))
        # applied_jobs_id = Application.objects.all().filter(user_id = user.id)
        # applied_jobs_id = Application.objects.all().filter(job__user_id=user.id)
        # print("list",applied_jobs_id)
        return Job.objects.filter(id__in=applied_jobs_id)
