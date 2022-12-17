from rest_framework import generics,viewsets, status
from rest_framework.decorators import action
from job.models.job import Job
from job.serializers.job import JobSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from job.services.job_service import JobService
from job.serializers.job import JobUserSerializer,JobUserStatusSerializer

class JobView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter()

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.filter()

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

    @action(methods=['GET'], detail=True)
    def job(self, request, pk=None):
        data = JobService.get_job_by_id(pk)
        if data!=None:
            data = JobUserSerializer(data).data
            return Response(data=data, status= status.HTTP_200_OK)
        else:
            return Response(dict(msg="Job is not existed"))

    @action(methods=['GET',],detail=False)
    def filter_job(self, request, *args, **kwargs):
        location = self.request.query_params.get('location',None)
        text = self.request.query_params.get('text',None)
        jobs = JobService.filter_job_by_location_and_text(location,text)
        data = JobSerializer(jobs,many=True).data
        return Response(data=data, status= status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def job_is_apply(self, request, *args, **kwargs):
        id_job = kwargs['pk']
        id_user = self.request.query_params.get('id_user',None)
        if id_job!= None and id_user!=None:
            try:
                data = JobService.get_job_with_status_by_id(id_job,id_user)
                data = JobUserStatusSerializer(data).data
                return Response(data=data, status= status.HTTP_200_OK)
            except:
                return Response(dict(msg="Job is not existed"))

    
