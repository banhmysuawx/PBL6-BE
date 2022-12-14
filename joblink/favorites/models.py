from django.db import models
from accounts.models import User
from job.models import Job
# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name="favorites")
    job = models.ForeignKey(Job , on_delete = models.CASCADE , related_name="jobs")

    class Meta:
        db_table = "favorites"
        