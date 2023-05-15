from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=33)
    price = models.DecimalField(max_digits=23, decimal_places=2)
    description = models.TextField()
    checkk = models.BooleanField(default=True)
