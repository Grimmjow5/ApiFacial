from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class Employee(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    nEmpleado = models.CharField(max_length=100)

    #vid = models.FileField(upload_to='video/')
