from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from companies.models import Company
from companies.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Favorite
from .serializers import FavoriteSerializer ,ListFavoriteJobSerializer

class ListJobFavoritesView(generics.ListAPIView):
    queryset_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    
class FavoriteView(generics.CreateAPIView):
    serializer_class = ListFavoriteJobSerializer
    queryset = Favorite.objects.all()

class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

class ListJobFavoritesView(APIView):
    serializer_class = FavoriteSerializer
    def get(self, request, *args, **kwargs):
        request.data["user"] = kwargs["user_id"]
        user_id_url = kwargs["user_id"]
        list_job_favorites_of_user = []
        list_job_favorites = Favorite.objects.all()
        for favorite in list_job_favorites:
            if favorite.user.id == user_id_url:
                list_job_favorites_of_user.append(favorite)
        serializer = FavoriteSerializer(list_job_favorites_of_user , many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

