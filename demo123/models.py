from django.db import models


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()


