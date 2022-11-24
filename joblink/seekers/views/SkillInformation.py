from rest_framework import generics,viewsets,status
from rest_framework.response import Response
from seekers.models import SkillInformation
from seekers.serializers.SkillInformation import SkillInformationSerializer

class SkillInformationView(generics.ListCreateAPIView):
    queryset = SkillInformation.objects.all()
    serializer_class = SkillInformationSerializer

class SkillInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillInformation.objects.all()
    serializer_class = SkillInformationSerializer

class SkillInProfile(viewsets.ViewSet):

    def list(self,request,*args, **kwargs):
        seeker_id = self.request.query_params.get('seeker_id')
        try:
            data = SkillInformation.objects.filter(seeker_id=seeker_id)
            data = SkillInformationSerializer(data,many=True).data
            return Response(data=data,status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


