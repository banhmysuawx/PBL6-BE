from rest_framework import generics
from seekers.models import ExpirenceInformation
from seekers.serializers.ExpirenceInformation import ExpirenceInformationSerializer

class ExpirenceInformationView(generics.ListCreateAPIView):
    queryset = ExpirenceInformation.objects.all()
    serializer_class = ExpirenceInformationSerializer

class ExpirenceInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpirenceInformation.objects.all()
    serializer_class = ExpirenceInformationSerializer