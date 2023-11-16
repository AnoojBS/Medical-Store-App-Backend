from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# class Medicine(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     remaining_stock = models.PositiveIntegerField(default=0)

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.CharField(max_length=5, null=True)
    expiry_date = models.DateField(null=True)
    description = models.TextField(null=True)


    def __str__(self):
        return self.name

