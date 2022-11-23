from rest_framework import generics
from seekers.models import EducationInformation
from seekers.serializers.EducationInformation import EducationInformationSerializer

class EducationInformationView(generics.ListCreateAPIView):
    queryset = EducationInformation.objects.all()
    serializer_class = EducationInformationSerializer

class EducationInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationInformation.objects.all()
    serializer_class = EducationInformationSerializer