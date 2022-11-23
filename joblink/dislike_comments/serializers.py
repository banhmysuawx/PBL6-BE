from dataclasses import field
from rest_framework import serializers
from .models import DisLikeComment
class DisLikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLikeComment
        fields = '__all__'