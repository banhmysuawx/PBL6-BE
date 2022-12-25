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

class GetCompany(APIView):
    def get(self, request, *args, **kwargs):
        company_list = []
        for company in Company.objects.all():
            round(company.average_rating['rating__avg'],2)
            company_list.append(company)
        serializer = CompanySerializer(company_list, many = True)
        print(company_list)
        return Response(serializer.data)
# API GET DETAIL COMPANY
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class TopCompanyListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        top_company_list = []
        for company in Company.objects.all():
            if round(float(company.average_rating['rating__avg']),1) > 4:
                top_company_list.append(company)
        serializer = CompanySerializer(top_company_list, many = True)
        return Response(serializer.data)

class CountCompanyView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request , format =None):
        sum_company = Company.objects.all().count()
        print(sum_company)
        return Response({'sum_company': sum_company})

class CompanyListAdminView(generics.ListCreateAPIView):
    serializer_class= CompanySerializer
    queryset = Company.objects.all()

class CompanyDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= CompanySerializer
    queryset = Company.objects.all()