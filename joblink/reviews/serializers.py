from rest_framework import serializers
from .models import Review

class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username', read_only=True)
    def get_author(self, object):
        return object.author.username
    class Meta:
        model = Review
        fields = ['id','rating','comment','company','user','created_at','author']