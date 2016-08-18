from __future__ import unicode_literals

from django.db import models
from teams.models import Member, Team

class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    latlon = models.CharField(max_length=255, blank=False, null=True)

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, blank=False)
    member = models.ForeignKey(Member, blank=False)
    comment = models.TextField(unique=True, blank=False)
    disliked = models.BooleanField(default=False)
    team = models.CharField(max_length=255, blank=False)
    datetime = models.DateTimeField(auto_now=True)

