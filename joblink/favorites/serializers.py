from dataclasses import fields
from rest_framework import serializers
from accounts.models import User
from job.models import Job
from .models import Favorite
from job.models import JobLocation
from job.models import JobSkill
from companies.models import Company

class ListFavoriteJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields ='__all__'
class FavoriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
class JobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = ['name','level_name','description']

class CompanyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','profile_description','established_date','image','company_name','company_location']

class JobLocationFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = ['location_name','street_address','city','state','country']

class FavoriteJobSerializer(serializers.ModelSerializer):
    locations = JobLocationFavoritesSerializer(many = True)
    skills = JobSkillSerializer(many = True)
    company = CompanyJobSerializer(many = False)
    class Meta:
        model = Job
        fields = ['id','name','salary','description','locations','skills','company']

class FavoriteSerializer(serializers.ModelSerializer):
    user = FavoriteUserSerializer(many = False)
    job = FavoriteJobSerializer(many = False)
    class Meta:
        model = Favorite
        fields = '__all__'

