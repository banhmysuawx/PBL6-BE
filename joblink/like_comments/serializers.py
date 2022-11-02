from dataclasses import field
from rest_framework import serializers
from like_comments.models import LikeComment
class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'