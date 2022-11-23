from rest_framework import serializers
from .models import Review
# from companies.serializers import CompanySerializer
from companies.models import Company
from accounts.models import User
from accounts.serializers import UserSerializer


class CompanyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','company_name','company_location','image']

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username', read_only=True)
    user = UserReviewSerializer()
    company = CompanyReviewSerializer()
    def get_author(self, object):
        return object.author.username
    class Meta:
        model = Review
        fields = ['id','rating','comment','company','user','created_at','author']

class ReviewCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('rating','comment','company')