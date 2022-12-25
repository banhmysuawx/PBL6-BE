from rest_framework import generics,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from seekers.models import SeekerProfile
from seekers.serializers.SeekerProfile import SeekerProfileSerializer, SeekerDetailSerializer
from seekers.services.SeekerProfile import SeekerProfileService

class SeekerProfileView(generics.ListCreateAPIView):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer

class SeekerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer

class SeekerProfileCandidateView(viewsets.ViewSet):

    @action(methods=['GET',],detail=False)
    def get_profile(self, request, *args, **kwargs):
        id_candidate = self.request.query_params.get("id_candidate",None)
        if id_candidate!=None:
            try:
                profile = SeekerProfile.objects.get(user_id=id_candidate)
                data = SeekerProfileSerializer(profile).data
                return Response(data=data,status=status.HTTP_200_OK)
            except:
                return Response(dict(msg="Profile is not existed"))
    
    @action(methods=['GET',],detail=False)
    def get_all_information(self, request, *args, **kwargs):
        try:
            data = SeekerProfileService.get_all_information()
            data = SeekerDetailSerializer(data, many=True).data
            return Response(data=data,status=status.HTTP_200_OK)
        except:
            return Response(dict(msg="Profile is not existed"))

    @action(methods=['GET',],detail=False)
    def get_all_information_user(self, request, *args, **kwargs):
        id_candidate = self.request.query_params.get("id_candidate",None)
        try:
            data = SeekerProfileService.get_all_information_by_id(id_candidate)
            data = SeekerDetailSerializer(data).data
            return Response(data=data,status=status.HTTP_200_OK)
        except:
            return Response(dict(msg="Profile is not existed"))
