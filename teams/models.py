from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Member(models.Model):
    user = models.ForeignKey(User, unique=True)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    connoisseur = models.BooleanField()
    team = models.ForeignKey(Team)
    
    USERNAME_FIELD = 'username'
