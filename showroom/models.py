from django.db import models


# Create your models here.
class Report(models.Model):
    name_us = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc_us = models.TextField()
    date = models.DateField()  

class showroom(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price= models.CharField(max_length=100)
    offer= models.BooleanField(default = False)

class Shop(models.Model):
    desc = models.TextField()
    paymentMethod = models.CharField(max_length=122)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField() 