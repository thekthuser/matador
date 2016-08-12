from django.shortcuts import render
from django.http import HttpResponse
from teams.forms import RegisterForm

# Create your views here.

def test_member(request):
    #return HttpResponse('view displays')
    #missing csrf
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('form saved')
    else:
        form = RegisterForm(initial = {'key': 'value'})
    return render(request, 'register.html', {'form': form})
