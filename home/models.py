from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(default=None,max_length = 50)
    email = models.CharField(default=None,max_length=50)
    phone = models.IntegerField(default=None)
    
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=None)