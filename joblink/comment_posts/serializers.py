from rest_framework import serializers
from .models import CommentPost
from accounts.models import User
class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )

class CommentPostSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only = True , many = False)
    sub_comments_list = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = CommentPost
        fields = ("user", "job","comment_body","is_sub_comment" , "parent_id", "id","created_at", "sub_comments_list")

    def get_sub_comments_list(self, instance):
        sub_comments = CommentPost.objects.filter(parent_id=instance.id)
        l = []
        for sub_comment in sub_comments:
            d = {}
            d["user"] = sub_comment.user.username
            d["comment_body"] = sub_comment.comment_body
            d["parent_id"] = sub_comment.parent_id
            d["id"] = sub_comment.id
            l.append(d)
        return l

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = ("user","job","comment_body","is_sub_comment","parent_id")
    def create(self, validated_data):
        return CommentPost.objects.create(**validated_data)

class EditCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = ("user","job","id","comment_body")

class DeleteCommentSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only = True , many = False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = CommentPost
        fields = ("user","job","id","comment_body","is_sub_comment","parent_id","created_at")