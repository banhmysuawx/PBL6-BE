from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from applicants.serializers.applicant import ApplicantSerializer
from applicants.models.applicant import Applicant

class ApplicantView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    parser_classes = [MultiPartParser,]