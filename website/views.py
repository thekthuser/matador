from django.shortcuts import render
from django.http import HttpResponse
from teams.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from restaurants.models import Restaurant, Review
from teams.models import Team, Member
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

#run once on fresh install to populate the db
def populate(request):
    valor = Team(name='Team Valor', description='Red team in Pokemon Go.')
    mystic = Team(name='Team Mystic', description='Blue team in Pokemon Go.')
    instinct = Team(name='Team Instinct', description='Yellow team in Pokemon Go.')
    valor.save()
    mystic.save()
    instinct.save()

    defaultMember = Member(username='defaultMember', password='', phone='555-5555', \
        email='default@example.com', connoisseur=True, team=valor)
    defaultMember.set_password('qwerty')
    defaultMember.save()

    shack = Restaurant(name='Shake Shack', description='Burgers.', \
        address='Grand Central Terminal, New York, NY 10017', latlon='40.7527233,-73.977262304')
    shack.save()

    shackReview = Review(restaurant=shack, member=defaultMember, comment='Long lines.', \
        disliked=False, team=valor.name)
    shackReview.save()

    return HttpResponse('Some sample data has been added. You may log in as "defaultMember" with the password "qwerty" or register a new account.')
