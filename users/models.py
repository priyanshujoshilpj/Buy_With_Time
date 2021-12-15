from django.db import models

# Create your models here.
class UserModel(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    pass1=models.CharField(max_length=20)