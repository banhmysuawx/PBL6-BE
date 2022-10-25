from tempfile import TemporaryFile
from unittest import result
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ( 
    ListCreateAPIView , 
    RetrieveUpdateDestroyAPIView,
)
from companies.models import Company
from companies.serializers import CompanySerializer
from accounts.models import User
from accounts.serializers import UserSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class CompanyListView(APIView):
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company , many = True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.data , status = status.HTTP_400_BAD_REQUEST)

# class CompanyDetail(APIView):

#     def get_object(self, id):
#         try: 
#             return Company.objects.get(id = id)
#         except Company.DoesNotExist:
#             return Response(data = "does not exist!" , status = status.HTTP_404_NOT_FOUND)
#     def get(self,request, id , format=None):
#         company = self.get_object(id)
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)
#     def put(self,request, id , format=None):
#         company = self.get_object(id)
#         serializer = CompanySerializer(company, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)