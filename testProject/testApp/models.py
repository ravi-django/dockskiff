from django.db import models


# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    price = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
