from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

#class Member(models.Model):
class Member(AbstractBaseUser):
    #user = models.ForeignKey(User, unique=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    connoisseur = models.BooleanField()
    team = models.ForeignKey(Team)
    
    USERNAME_FIELD = 'username'

    objects = UserManager()
