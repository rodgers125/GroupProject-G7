from django.db import models


# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    message = models.TextField()


class User(models.Model):
    country = models.CharField(max_length=100, blank=False)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    zip = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
