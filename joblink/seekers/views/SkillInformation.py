from rest_framework import generics
from seekers.models import SkillInformation
from seekers.serializers.SkillInformation import SkillInformationSerializer

class SkillInformationView(generics.ListCreateAPIView):
    queryset = SkillInformation.objects.all()
    serializer_class = SkillInformationSerializer

class SkillInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillInformation.objects.all()
    serializer_class = SkillInformationSerializer