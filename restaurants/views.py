from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from restaurants.forms import AddRestaurantForm
from restaurants.models import Restaurant

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
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/view_restaurants.html', {'restaurants': restaurants})
