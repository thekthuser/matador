from django import forms
from django.forms import ModelForm
from restaurants.models import Restaurant, Review, Visit
from teams.models import Member
import datetime

class AddRestaurantForm(ModelForm):
    
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address']

        def save(self, commit=True):
            res = super(AddRestaurantForm, self).save(commit=False)
            res.name = self.cleaned_data.get('name')
            res.description = self.cleaned_data.get('description')
            res.address = self.cleaned_data.get('address')
            #res.latlon

            if commit:
                res.save()
            return res

class AddReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['comment']


    #this is here so I can pass restaurant and member from the view
    def __init__(self, *args, **kwargs):
        self.restaurant = kwargs.pop('restaurant', None)
        self.member = kwargs.pop('member', None)
        super(AddReviewForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        review = super(AddReviewForm, self).save(commit=False)
        #check if these can be saved directly instead of looking up with pk
        review.res = Restaurant.objects.get(pk=restauarant.id)
        review.member = Member.objects.get(pk=member.id)
        review.comment = self.cleaned_data.get('comment')
        review.datetime = datetime.datetime.now()

        if commit:
            review.save()
        return review
