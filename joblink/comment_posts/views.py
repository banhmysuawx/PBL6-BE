from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import CommentPost
from .serializers import CommentPostSerializer ,AddCommentSerializer,EditCommentSerializer,DeleteCommentSerializer

# LIST COMMENT POST
class CommentListView(APIView):
    serializer_class = CommentPostSerializer
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        comments = CommentPost.objects.filter(is_sub_comment=False)
        sub_comments_dict = {}
        for comment in comments:
            sub_comments_dict[comment.id] = CommentPost.objects.filter(parent_id=comment.id)
        serializer = CommentPostSerializer(comments, many=True)
        return Response(serializer.data)

# ADD COMMENT POST
class AddCommentAPI(APIView):
    serializer_class = AddCommentSerializer
    permission_class = (IsAuthenticatedOrReadOnly,)
    
    def post(self, request, format=None):
        data = request.data
        serializer = AddCommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# UPDATE COMMENT POST
class EditCommentAPI(generics.UpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = EditCommentSerializer
    queryset = CommentPost.objects.all()

# DELETE COMMENT POST
class DeleteCommentAPI(generics.DestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = DeleteCommentSerializer
    queryset = CommentPost.objects.all()
