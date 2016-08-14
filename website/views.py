from django.shortcuts import render
from django.http import HttpResponse
from teams.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('form saved')
    else:
        form = RegisterForm(initial = {'key': 'value'})
    return render(request, 'website/register.html', {'form': form})


@login_required(login_url = reverse_lazy('login'))
def index(request):
    return render(request, 'website/index.html')
