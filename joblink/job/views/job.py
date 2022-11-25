from rest_framework import generics,viewsets, status
from rest_framework.decorators import action
from job.models.job import Job
from job.serializers.job import JobSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from job.services.job_service import JobService
from job.serializers.job import JobUserSerializer

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

class JobInCompanyView(viewsets.ViewSet):
    
    @action(methods=['GET'],detail=False)
    def get_jobs(self,request, *args, **kwargs):
        id_company = self.request.query_params.get("company_id", None)
        if id_company != None:
            data = Job.objects.filter(company_id=id_company)
            data = JobSerializer(data,many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class JobListAdminView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True)

class JobDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter(is_active=True)

class JobInUserView(viewsets.ViewSet):

    @action(methods=['GET'], detail=False)
    def get_jobs(self, request, *args, **kwargs):
        data = JobService.get_job_to_show_candidate()
        data = JobUserSerializer(data, many=True).data
        return Response(data=data, status= status.HTTP_200_OK)
    
