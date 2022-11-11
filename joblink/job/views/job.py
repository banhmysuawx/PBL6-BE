from rest_framework import generics
from job.models.job import Job
from job.serializers.job import JobSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
class JobView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True)

class SumJobView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request , format =None):
        sum_job = Job.objects.all().count()
        return Response({'count': sum_job})