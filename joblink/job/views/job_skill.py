from rest_framework import generics
from job.models.job_skill import JobSkill
from job.serializers.job_skill import JobSkillSerializer

class JobSkillView(generics.ListCreateAPIView):
    serializer_class = JobSkillSerializer
    queryset = JobSkill.objects.all()

class JobSkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSkillSerializer
    queryset = JobSkill.objects.all()