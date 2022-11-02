from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import DisLikeComment
from .serializers import DisLikeCommentSerializer

class DisLikeCommentListAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class= DisLikeCommentSerializer
    queryset = DisLikeComment.objects.all()