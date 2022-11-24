from rest_framework import generics,viewsets,status
from rest_framework.response import Response
from seekers.models import EducationInformation
from seekers.serializers.EducationInformation import EducationInformationSerializer

class EducationInformationView(generics.ListCreateAPIView):
    queryset = EducationInformation.objects.all()
    serializer_class = EducationInformationSerializer

class EducationInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationInformation.objects.all()
    serializer_class = EducationInformationSerializer

class EducationInProfile(viewsets.ViewSet):

    def list(self,request,*args, **kwargs):
        seeker_id = self.request.query_params.get('seeker_id')
        try:
            data = EducationInformation.objects.filter(seeker_id=seeker_id)
            data = EducationInformationSerializer(data,many=True).data
            return Response(data=data,status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

