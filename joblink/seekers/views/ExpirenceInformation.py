from rest_framework import generics,viewsets,status
from rest_framework.response import Response
from seekers.models import ExpirenceInformation
from seekers.serializers.ExpirenceInformation import ExpirenceInformationSerializer

class ExpirenceInformationView(generics.ListCreateAPIView):
    queryset = ExpirenceInformation.objects.all()
    serializer_class = ExpirenceInformationSerializer

class ExpirenceInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpirenceInformation.objects.all()
    serializer_class = ExpirenceInformationSerializer

class ExpirenceInProfile(viewsets.ViewSet):

    def list(self,request,*args, **kwargs):
        seeker_id = self.request.query_params.get('seeker_id')
        try:
            data = ExpirenceInformation.objects.filter(seeker_id=seeker_id)
            data = ExpirenceInformationSerializer(data,many=True).data
            return Response(data=data,status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


