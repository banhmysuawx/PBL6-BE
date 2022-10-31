from rest_framework import serializers
from companies.models import Company
from reviews.serializers import ReviewsSerializer

class CompanySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    reviews = ReviewsSerializer(many = True)
    def get_average_rating(self, obj):
        return obj.average_rating
    class Meta:
        model = Company
        fields = ('id','profile_description','established_date','image','company_name','company_location','average_rating','reviews')