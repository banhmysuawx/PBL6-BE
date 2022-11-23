from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import LikeComment
from .serializers import LikeCommentSerializer

# class LikeCommentListAPI(APIView):
#     def get(self,request,pk):#function to get total number of likes to particular post
#         post = LikeComment.objects.filter(pk=pk) # find which post's likes are to be extracted
#         like_count = post.like_comment.count()
#         serializer = LikeCommentSerializer(like_count,many=True)
#         return Response(serializer.data)
class LikeCommentListAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class= LikeCommentSerializer
    queryset = LikeComment.objects.all()