from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from companies.models import Company
from companies.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics

# class SeekerAndCompanyChart(APIView):
#     seekerList = []
#     for seeker in User.objects.all():