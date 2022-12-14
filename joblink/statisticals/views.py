from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from companies.models import Company
from job.models import Job
from job.models import JobCategory
from collections import defaultdict
# Create your views here.
class TopCompany(APIView):

    permission_classes = []
    def get(self, request, format =None):
        labels = []
        chartLabels = "Top Company"
        chartData = []
        list_all_companies = Company.objects.all()
        for company in list_all_companies:
            if float(company.average_rating['rating__avg']) > 4:
                labels.append(company.company_name)
                chartData.append(round(company.average_rating['rating__avg'],1))
        print("labels" , labels)
        print("chartData" , chartData)
        data = {
            "labels":labels,
            "chartLabels":chartLabels,
            "chartData":chartData
        }
        return Response(data,status=status.HTTP_200_OK)

class TopJobCategory(APIView):
    permission_classes=[]

    def get(self, request , format=None):
        category_job_name = [] # list category each job
        job_name = [] # list job names
        labels = [] 
        chartLabels = "The Most Job Category Populator"
        chartData = []
        # Using loop to get category name and job name
        for job in Job.objects.all():
            if job != None:
                category_job_name.append(job.category.name)
                job_name.append(job.name)

        # Create default dict
        d = defaultdict(list)
        for key, value in zip(category_job_name, job_name):
            d[key].append(value)

        # Using loop to get labelsChart and chartData
        for new_k, new_val in d.items():
            labels.append(new_k)
            chartData.append(len([item for item in new_val if item]))
        
        data = {
            "chartLabels":chartLabels,
            "labels":labels,
            "chartData":chartData
        }

        return Response(data, status=status.HTTP_200_OK)

class TopJobHighSalary(APIView):
    def get(self, request, format =None):
        permission_classes = []
        labels = [] 
        chartLabels = "The Most Job High Salary"
        chartData = []
        for job in Job.objects.all():
            if round(float(job.salary),1) > 2000:
                labels.append(job.name)
                chartData.append(job.salary)
        data = {
            "chartLabels":chartLabels,
            "labels":labels,
            "chartData":chartData
        }
        return Response(data, status=status.HTTP_200_OK)