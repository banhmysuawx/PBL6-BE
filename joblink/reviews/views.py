from django.shortcuts import render
from .models import Review
from .serializers import ReviewsSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics

# API GET and POST REVIEW
class ReviewListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class= ReviewsSerializer
    queryset = Review.objects.all()

# API GET DETAIL REVIEW
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewsSerializer
    queryset = Review.objects.all()
