from __future__ import unicode_literals

from django.db import models
from teams.models import Member, Team

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latlon = models.CharField(max_length=255)
    #timesVisited = models.IntegerField(max_length=255)

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    member = models.ForeignKey(Member)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

#record of visits so thumbsDown can be different for different teams
class Visit(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    team = models.ForeignKey(Team)
    thumbDown = models.BooleanField()
    datetime = models.DateTimeField(auto_now=True)
