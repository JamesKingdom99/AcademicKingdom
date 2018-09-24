from django.db import models

# Create your models here.
class Student(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
