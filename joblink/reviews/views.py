from django.shortcuts import render
from .models import Review
from .serializers import ReviewsSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# API GET REVIEW
class ReviewsListAPI(APIView):
    def get(self , request , format =None):
        review = Review.objects.all()
        serializer = ReviewsSerializer(review , many = True)
        return Response(serializer.data)

# API CREATE REVIEW
class ReviewsCreateAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = ReviewsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.data , status = status.HTTP_400_BAD_REQUEST)

# API GET COMPANY DETAIL
class ReviewsDetailAPI(APIView):
    permission_classes = (AllowAny,)
    def get_object(self, id):
        try: 
            return Review.objects.get(id = id)
        except Review.DoesNotExist:
            return Response(data = "does not exist!" , status = status.HTTP_404_NOT_FOUND)
    def get(self,request, id , format=None):
        review = self.get_object(id)
        serializer = ReviewsSerializer(review)
        return Response(serializer.data)

# API PUT COMPANY
class ReviewsUpdateAPI(APIView):
    permission_classes = (AllowAny,)
    def put(self,request, id , format=None):
        review = self.get_object(id)
        serializer = ReviewsSerializer(review, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
# API DELETE COMPANY
class ReviewsDeleteAPI(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request, id, format=None):
        review = self.get_object(id)
        review.delete()
        return Response(data = "Deleted OK!",status=status.HTTP_204_NO_CONTENT)