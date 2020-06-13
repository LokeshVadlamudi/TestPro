from django.db import models



# Create your models here.

class User(models.Model):
    userName = models.CharField('User Name', max_length=100)
    password = models.CharField('Password', max_length=100)
