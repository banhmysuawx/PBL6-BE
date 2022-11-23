from rest_framework import generics,viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from job.models.job_skill import JobSkill
from job.serializers.job_skill import JobSkillSerializer
from job.services.job_skill_service import JobSkillService

class JobSkillView(generics.ListCreateAPIView):
    serializer_class = JobSkillSerializer
    queryset = JobSkill.objects.all()

class JobSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSkillSerializer
    queryset = JobSkill.objects.all()

class JobSkillInCompanyView(viewsets.ViewSet):
   

    @action(methods=['GET'], detail=False)
    def get_skills(self,request,*args, **kwargs):
        id_company = self.request.query_params.get('company_id',None)
        if id_company != None:
            data = JobSkillService.getSkills(id_company)
            data = JobSkillSerializer(data, many=True).data
            return Response(data=data, status = status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

