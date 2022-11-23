from django.db import models
from accounts.models import User
from comment_posts.models import CommentPost

class DisLikeComment(models.Model):
    dislike_user = models.ManyToManyField(User)
    dislike_comment = models.ForeignKey(CommentPost , on_delete=models.CASCADE , related_name = "dislike_comments")

    class Meta:
        db_table = "like_comments"