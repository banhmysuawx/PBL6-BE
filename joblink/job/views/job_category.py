from rest_framework import generics,mixins
from job.serializers.job_category import JobCategorySerializer
from job.models.job_category import JobCategory

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

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs )


