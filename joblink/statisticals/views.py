from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Count
from rest_framework import generics
from companies.models import Company
from job.models import Job
from job.models import JobCategory
from collections import defaultdict
from accounts.models import User
from django.db.models import Func
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
import json
from django.http import HttpResponse
from reviews.models import Review
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

def Extract(field, date_field='DOW'):
    template = "EXTRACT({} FROM %(expressions)s::timestamp)".format(date_field)
    return Func(field, template=template)

class SeekerAndEmployerByMonth(APIView):
    def get(self, request, format =None):
        labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
        seekerList = list(User.objects.filter(role='seeker').annotate(month=TruncMonth('created_at')).values('month').annotate(count_id=Count('id')).order_by('-month')[:12])
        employerList = list(User.objects.filter(role='employer').annotate(month=TruncMonth('created_at')).values('month').annotate(count_id=Count('id')).order_by('-month')[:12])
        seeker_count = []
        seeker_count = [0 for i in range(12)] 
        employer_count = []
        employer_count = [0 for i in range(12)]
        for user in seekerList:
            if  user['month'].month == 1:
                seeker_count[0]=user['count_id']
            elif user['month'].month == 2:
                seeker_count[1]=user['count_id']
            elif user['month'].month == 3:
                seeker_count[2]=user['count_id']
            elif user['month'].month == 4:
                seeker_count[3]=user['count_id']
            elif user['month'].month == 5:
                seeker_count[4]=user['count_id']
            elif user['month'].month == 6:
                seeker_count[5]=user['count_id']
            elif user['month'].month == 7:
                seeker_count[6]=user['count_id']
            elif user['month'].month == 8:
                seeker_count[7]=user['count_id']
            elif user['month'].month == 9:
                seeker_count[8]=user['count_id']
            elif user['month'].month == 10:
                seeker_count[9]=user['count_id']
            elif user['month'].month == 11:
                seeker_count[10]=user['count_id']
            elif user['month'].month == 12:
                seeker_count[11]=user['count_id']
        for user in employerList:
            if  user['month'].month == 1:
                employer_count[0]=user['count_id']
            elif user['month'].month == 2:
                employer_count[1]=user['count_id']
            elif user['month'].month == 3:
                employer_count[2]=user['count_id']
            elif user['month'].month == 4:
                employer_count[3]=user['count_id']
            elif user['month'].month == 5:
                employer_count[4]=user['count_id']
            elif user['month'].month == 6:
                employer_count[5]=user['count_id']
            elif user['month'].month == 7:
                employer_count[6]=user['count_id']
            elif user['month'].month == 8:
                employer_count[7]=user['count_id']
            elif user['month'].month == 9:
                employer_count[8]=user['count_id']
            elif user['month'].month == 10:
                employer_count[9]=user['count_id']
            elif user['month'].month == 11:
                employer_count[10]=user['count_id']
            elif user['month'].month == 12:
                employer_count[11]=user['count_id']

        data = {
            "labels":labels,
            "seeker":seeker_count,
            "employer":employer_count
        }

        return Response(data, status=status.HTTP_200_OK)

class RatingCompany(APIView):
    def get(self, request, *args, **kwargs):
        company_id = self.kwargs.get('id_company')
        company_object = Company.objects.filter(id = company_id)
        reviews_in_company = list(company_object)
        rating_one = 0
        rating_two = 0
        rating_three = 0
        rating_four = 0
        rating_five = 0
        rating_in_company = []
        list_review_of_company = list(Company.objects.filter(id = company_id).values_list('reviews', flat = True))
        for index in range(len(list_review_of_company)):
            for item in Review.objects.all():
                if item.id == list_review_of_company[index]:
                    rating = item.rating
                    rating_in_company.append(rating)
        for item in rating_in_company:
            if item == 1 :
                rating_one = rating_one + 1
            elif item == 2 :
                rating_two = rating_two + 1
            elif item == 3 :
                rating_three = rating_three + 1
            elif item == 4 :
                rating_four = rating_four + 1
            elif item == 5 :
                rating_five = rating_five + 1
        data = {
            'rating_one': rating_one,
            'rating_two': rating_two,
            'rating_three': rating_three,
            'rating_four': rating_four,
            'rating_five': rating_five           
        }
        print("Review of company",rating_in_company)
        print("Review",list_review_of_company)
        print("Company" , reviews_in_company)
        return Response(data,status=status.HTTP_200_OK)
