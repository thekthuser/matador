from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from restaurants.forms import AddRestaurantForm, AddReviewForm
from restaurants.models import Restaurant
from teams.models import Member

# Create your views here.

#come back and restrict this to logged in connoisseurs
@login_required(login_url = reverse_lazy('login'))
def add_restaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/index.html')
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
    return render(request, 'restaurants/view_restaurant.html', {'restaurant': restaurant})


@login_required(login_url = reverse_lazy('login'))
#pk is id of review's restaurant
def add_review(request, pk):
    if request.method == 'POST':
        restaurant = Restaurant.objects.get(id=pk)
        form = AddReviewForm(request.POST, restaurant=restaurant, member=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'website/index.html')
    else:
        form = AddReviewForm(initial = {'key': 'value'})
    return render(request, 'restaurants/add_review.html', {'form': form, 'pk': pk})
