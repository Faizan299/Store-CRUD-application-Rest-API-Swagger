from django.db import models

class Store(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

class Products(models.Model):
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
