from django.db import models
from accounts.models import User
from django.db.models import Avg
from django.db.models import Func
# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User ,on_delete = models.CASCADE , related_name="company")
    profile_description = models.TextField(max_length = 256 , blank=True , default='')
    established_date =  models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank = True , default='')
    company_name = models.CharField(max_length= 256, blank=True , default='')
    company_location = models.CharField(max_length = 256 , blank=True , default='')
    def __str__(self):
        return self.company_name
    
    @property
    def average_rating(self):
        if hasattr(self, '_average_rating'):
            return self._average_rating
        return self.reviews.aggregate(Avg('rating'))

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 2)'