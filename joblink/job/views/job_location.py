from rest_framework import generics
from job.serializers.job_location import JobLocationSerializer
from job.models.job_location import JobLocation

class JobLocationView(generics.ListCreateAPIView):
    serializer_class= JobLocationSerializer
    queryset = JobLocation.objects.all()

class JobLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= JobLocationSerializer
    queryset = JobLocation.objects.all()
