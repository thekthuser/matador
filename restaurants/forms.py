from django import forms
from django.forms import ModelForm
from restaurants.models import Restaurant, Review
from teams.models import Member
import datetime
from geopy.geocoders import Nominatim

class AddRestaurantForm(ModelForm):
    
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address']

    def save(self, commit=True):
        res = super(AddRestaurantForm, self).save(commit=False)
        res.name = self.cleaned_data.get('name')
        res.description = self.cleaned_data.get('description')
        res.address = self.cleaned_data.get('address')
        
        geolocator = Nominatim()
        # .geocode returns None if address not found, but sometimes still geocodes bad addresses
        # for example, it thinks the address 'bad address' is in dubai...
        loc = geolocator.geocode(res.address, timeout=None)
        if loc:
            res.latlon = str(loc.latitude) + ',' + str(loc.longitude)
        else:
            res.latlon = None

        if commit:
            res.save()
        return res

class AddReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['comment', 'disliked']


    #this is here so I can pass restaurant and member from the view
    def __init__(self, *args, **kwargs):
        self.restaurant = kwargs.pop('restaurant', None)
        self.member = kwargs.pop('member', None)
        super(AddReviewForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        review = super(AddReviewForm, self).save(commit=False)
        review.restaurant = self.restaurant
        review.member = self.member
        review.comment = self.cleaned_data.get('comment')
        review.disliked = self.cleaned_data.get('disliked')
        review.datetime = datetime.datetime.now()

        if commit:
            review.save()
        return review
