from django.shortcuts import render
from django.http import HttpResponse
from teams.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from restaurants.models import Restaurant, Review
from django.db.models import Q

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/index.html', {'success': True})
    else:
        form = RegisterForm(initial = {'key': 'value'})
    return render(request, 'website/register.html', {'form': form})


@login_required(login_url = reverse_lazy('login'))
def index(request):
    review_count = Review.objects.all().filter(member=request.user.id).count()
    res_count = Restaurant.objects.all().filter(Q(review__member=request.user.id)).count()
    return render(request, 'website/index.html', {'review_count': review_count, 'res_count': res_count})

#used to test if a user is authorized to add a new restaurant
def user_is_connoisseur(user):
    return user.is_authenticated() and user.connoisseur
