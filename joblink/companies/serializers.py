from rest_framework import serializers
from companies.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','profile_description','established_date','image','company_name','company_location')
