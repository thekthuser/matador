from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

#teams allow for disliked restaurants to apply only to that team
#actual dislike status is stored in reviews
class Team(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

#Member class replaces User, with a few extra fields
class Member(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, unique=True, blank=False)
    #connoisseur status allows adding new restaurants
    connoisseur = models.BooleanField(default=False)
    team = models.ForeignKey(Team)
    
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __unicode__(self):
        return self.username
