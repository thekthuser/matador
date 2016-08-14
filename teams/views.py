from django.shortcuts import render
#from django.core.context_processors import csrf
from django.http import HttpResponse
from teams.forms import RegisterForm
from teams.models import Team, Member
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def test_member(request):
    #return HttpResponse('view displays')
    #missing csrf
    #c = {}
    #c.update(csrf(request))
    """
    testTeam = Team(name='Team Valor')
    testTeam.save()
    return HttpResponse('created team')
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print repr(form)
        print form.is_valid()
        if form.is_valid():
            form.save()
            return HttpResponse('form saved')
    else:
        form = RegisterForm(initial = {'key': 'value'})
    return render(request, 'teams/register.html', {'form': form})

def login_member(request):
    return HttpResponse('login_member')

@login_required(login_url = reverse_lazy('login'))
def index(request):
    return HttpResponse('logged in to index page')
