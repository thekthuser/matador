from __future__ import unicode_literals

from django.db import models
from teams.models import Member, Team

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    latlon = models.CharField(max_length=255, blank=False, null=True)
    #timesVisited = models.IntegerField(max_length=255)

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=False)
    member = models.ForeignKey(Member, blank=False)
    comment = models.TextField(unique=True, blank=True)
    disliked = models.BooleanField(default=False)
    team = models.CharField(max_length=255, blank=False)
    datetime = models.DateTimeField(auto_now=True)

#record of visits so thumbsDown can be different for different teams
#just realized i can put thumbsDown in the Review instead, will delete later
class Visit(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    team = models.ForeignKey(Team)
    thumbDown = models.BooleanField()
    datetime = models.DateTimeField(auto_now=True)
