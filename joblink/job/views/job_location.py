from rest_framework import generics,status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from job.serializers.job_location import JobLocationSerializer
from job.models.job_location import JobLocation
from job.services.job_location_service import JobLocationService


class JobLocationView(generics.ListCreateAPIView):
    serializer_class= JobLocationSerializer
    queryset = JobLocation.objects.all()

class JobLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= JobLocationSerializer
    queryset = JobLocation.objects.all()

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