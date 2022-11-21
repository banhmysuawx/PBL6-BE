from rest_framework import generics,mixins
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from job.serializers.job_category import JobCategorySerializer
from job.models.job_category import JobCategory
from job.services.job_category_service import JobCategoryService
from job.serializers.job_category import getJobCategorySerializer


class JobCategoryView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()

    def get(self,request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    
class JobCategoryDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs )

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request,*args, **kwargs )

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs )


class CategoryJobInCompany(viewsets.ViewSet):
    serializer_class = JobCategorySerializer
    queryset = JobCategory.objects.all()

    @action(methods=['GET'],detail=False)
    def get_category_and_job(self, request, *args, **kwargs):
        id_company = self.request.query_params.get("company_id", None)
        if id_company != None :
            data = JobCategoryService.getJob(id_company)
            data = getJobCategorySerializer(data,many=True).data
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'],detail=False)
    def get_category(self, request, *args, **kwargs):
        id_company = self.request.query_params.get("company_id", None)
        if id_company != None :
            data = JobCategoryService.getCategoryInCompany(id_company)
            data = JobCategorySerializer(data,many=True).data
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




    