from django.db import models
from accounts.models import User
from job.models import Job
# Create your models here.
class CommentPost(models.Model):
    user = models.ForeignKey(User,  related_name = "comments",on_delete = models.CASCADE)
    job = models.ForeignKey(Job,related_name = "comments", on_delete = models.CASCADE)
    comment_body = models.TextField(blank =True , null = True)
    is_sub_comment = models.BooleanField()
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table = "comment_posts"