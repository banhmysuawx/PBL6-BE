from dataclasses import fields
from rest_framework import serializers
from accounts.models import User
from job.models import Job
from .models import Favorite
from job.models import JobLocation
class FavoriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class JobLocationFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = ['location_name','street_address','city','state','country']

class FavoriteJobSerializer(serializers.ModelSerializer):
    locations = JobLocationFavoritesSerializer(many = True)
    class Meta:
        model = Job
        fields = ['name','salary','description','locations']

class FavoriteSerializer(serializers.ModelSerializer):
    user = FavoriteUserSerializer(many = False)
    job = FavoriteJobSerializer(many = False)
    class Meta:
        model = Favorite
        fields = '__all__'

