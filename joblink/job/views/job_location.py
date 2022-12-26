from rest_framework import generics,status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from job.serializers.job_location import JobLocationSerializer
from job.models.job_location import JobLocation
from job.models.job import Job
from job.services.job_location_service import JobLocationService
from django.db.models import Q


class JobLocationView(generics.ListCreateAPIView):
    serializer_class= JobLocationSerializer
    queryset = JobLocation.objects.all()

class JobLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= JobLocationSerializer
    queryset = JobLocation.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            num_jobs = Job.objects.filter(locations__id = instance.id).count()
            if (num_jobs==0):
                self.perform_destroy(instance)
                return Response(dict(msg="Delete Location successful",status=status.HTTP_200_OK))
            else:
                return Response(dict(msg="Location is used. Don't delete it",status=status.HTTP_204_NO_CONTENT))
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

class JobLocationInCompanyView(viewsets.ViewSet):
    queryset = JobLocation.objects.all()
    serializer_class = JobLocationSerializer
    
    @action(methods=['GET'],detail=False)
    def get_location(self,request,*args, **kwargs):
        id_company = self.request.query_params.get("company_id", None)
        if id_company != None:
            data = JobLocationService.getLocationInCompany(id_company)
            data = JobLocationSerializer(data, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'],detail=False)
    def filter(self,request,*args, **kwargs):
        id_company = self.request.query_params.get("company_id", None)
        text = self.request.query_params.get("text", '')
        if id_company != None:
            data = JobLocation.objects.filter(company_id=id_company).filter(Q(location_name__icontains=text) | Q(street_address__icontains=text) | Q(city__icontains=text))
            data = JobLocationSerializer(data, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)