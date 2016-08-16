from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from restaurants.forms import AddRestaurantForm, AddReviewForm
from restaurants.models import Restaurant, Review
from teams.models import Member

# Create your views here.

#come back and restrict this to logged in connoisseurs
@login_required(login_url = reverse_lazy('login'))
def add_restaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            # after add_restauarant, send to add_review to post first review
            reviewForm = AddReviewForm()
            addedRes = Restaurant.objects.get(name=form.cleaned_data.get('name'))
            return render(request, 'restaurants/add_review.html', \
                {'first': True, 'form': reviewForm, 'pk': addedRes.id})
    else:
        form = AddRestaurantForm(initial = {'key': 'value'})
    return render(request, 'restaurants/add_restaurant.html', {'form': form})

@login_required(login_url = reverse_lazy('login'))
def view_restaurants(request):
    #restaurants = Restaurant.objects.all().filter(disliked=False)
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/view_restaurants.html', {'restaurants': restaurants})

@login_required(login_url = reverse_lazy('login'))
def view_restaurant(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    reviews = Review.objects.all().filter(restaurant=pk)
    return render(request, 'restaurants/view_restaurant.html', \
            {'restaurant': restaurant, 'reviews': reviews})


@login_required(login_url = reverse_lazy('login'))
#pk is id of review's restaurant
def add_review(request, pk):
    if request.method == 'POST':
        restaurant = Restaurant.objects.get(id=pk)
        form = AddReviewForm(request.POST, restaurant=restaurant, member=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'website/index.html', {'success': True})
    else:
        form = AddReviewForm(initial = {'key': 'value'})
    return render(request, 'restaurants/add_review.html', {'form': form, 'pk': pk})
