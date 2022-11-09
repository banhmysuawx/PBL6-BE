from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from applications.serializers import ApplyJobSerializer , ApplicantSerializer,AppliedJobSerializer
from applications.models import Application
from job.models import Job

class ApplyJobApiView(CreateAPIView):
    serializer_class = ApplyJobSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # queryset = Application.objects.all()


class AppliedJobsAPIView(ListAPIView):
    serializer_class = AppliedJobSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        print("user",user)
        applied_jobs_id = list(Application.objects.filter(user=user.id))
        # print("list",applied_jobs_id)
        return Job.objects.filter(id__in=applied_jobs_id)
