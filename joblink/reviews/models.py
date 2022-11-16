from django.db import models
from companies.models import Company
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Review(models.Model):
    rating = models.SmallIntegerField( default=0,validators=[MaxValueValidator(5),MinValueValidator(1)])
    comment = models.CharField(max_length=500)
    company = models.ForeignKey(Company , on_delete = models.CASCADE ,  related_name="reviews")
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name="reviews")
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f'Review by {self.user.username} on {self.company.company_name}'

    def author(self):
        return self.user.username