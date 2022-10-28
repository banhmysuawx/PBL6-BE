from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework import status
from companies.models import Company
from companies.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# API GET
class CompanyListView(APIView):

    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)
        return Response(serializer.data)

# API POST COMPANY
class CompanyCreateAPI(APIView):
    def post(self, request, format=None):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.data , status = status.HTTP_400_BAD_REQUEST)

# API GET DETAIL COMPANY
class CompanyDetail(APIView):
    permission_classes = (AllowAny,)
    def get_object(self, id):
        try: 
            return Company.objects.get(id = id)
        except Company.DoesNotExist:
            return Response(data = "does not exist!" , status = status.HTTP_404_NOT_FOUND)
    def get(self,request, id , format=None):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

# API PUT COMPANY
class CompanyUpdate(APIView):
    permission_classes = (AllowAny,)
    def put(self,request, id , format=None):
        company = self.get_object(id)
        serializer = CompanySerializer(company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# API DELETE COMPANY
class CompanyDelete(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request, id, format=None):
        company = self.get_object(id)
        company.delete()
        return Response(data = "Deleted OK!",status=status.HTTP_204_NO_CONTENT)
