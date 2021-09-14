from django.db import models

# Create your models here.

class Customers(models.Model):
    # SEX_CHOICES = (
    #     ('M' , 'Male'),
    #     ('F', 'Female')
    # )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    # sex_choices = models.CharField(max_length=50, choices=SEX_CHOICES)

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    in_Stock = models.IntegerField()
    price = models.FloatField()


    
class Order_items(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    datetime_stamp = models.DateTimeField(auto_now_add=True)
    quantity = models.TextField()

    

class Order(models.Model):
    shipping_address = models.TextField()
    billing_address = models.TextField()
    time_fulfilled = models.DateTimeField(auto_now_add=True)

    
