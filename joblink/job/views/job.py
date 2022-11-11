from rest_framework import generics
from job.models.job import Job
from job.serializers.job import JobSerializer

class JobView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True)