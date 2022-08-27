from django.db import models

# Create your models here.
class RestaurantAccount(models.Model):
    restaurant_name = models.CharField(max_length=50)
    restaurant_Address = models.CharField(max_length=50)
    restaurant_Contact = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='media/RLogo/')

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    restaurant_id = models.IntegerField()

class Product(models.Model):
    category_name = models.CharField(max_length=250)
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField()
    status = models.BooleanField(default=True)
    restaurant_id = models.IntegerField()
    image = models.ImageField(upload_to='media/media/PImage/')

class Table(models.Model):
    table_name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    restaurant_id = models.IntegerField()

