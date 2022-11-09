from django.db import models
from django.utils import timezone
from accounts.models import User 
from job.models import Job

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job,related_name = "applies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=256 , blank = True, default='')
    email = models.EmailField(max_length=256 , blank = True, default= '')
    cv = models.FileField(default = None , blank = True) 
    cover_letter = models.TextField(max_length= 500 , blank = True, default = '')
    status = models.SmallIntegerField(default=1)
    test_result = models.FloatField(blank=True , default =  0.0)
    class Meta:
        ordering = ["id"]
        db_table = "applications"
        unique_together = ["user", "job"]
    def __str__(self):
        return self.fullname
    @property
    def get_status(self):
        if self.status == 1:
            return "Pending"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"