from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from companies.models import Company
from companies.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics

# API GET and POST requests
class CompanyListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class= CompanySerializer
    queryset = Company.objects.all()

# API GET DETAIL COMPANY
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
