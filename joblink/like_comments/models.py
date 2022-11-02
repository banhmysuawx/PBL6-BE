from django.db import models
from accounts.models import User
from comment_posts.models import CommentPost

class LikeComment(models.Model):
    like_user = models.ManyToManyField(User)
    like_comment = models.ForeignKey(CommentPost , on_delete=models.CASCADE , related_name = "like_comments")
    