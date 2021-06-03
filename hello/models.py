from django.db import models

# Create your models here.
from os import name


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()
    def __str__(self):
        return (self.name)

class Books(models.Model):
    name=models.CharField(max_length=200)
    owner=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='store/pdf/')
    

    def __str__(self):
        return (self.name)
