from rest_framework import generics
from seekers.models import SeekerProfile
from seekers.serializers.SeekerProfile import SeekerProfileSerializer

class SeekerProfileView(generics.ListCreateAPIView):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer

class SeekerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer