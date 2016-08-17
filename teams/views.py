from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from teams.forms import EditMemberForm, AddTeamForm

@login_required(login_url = reverse_lazy('login'))
def edit_member(request):
    if request.method == 'POST':
        form = EditMemberForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'website/index.html', {'success': True})
    else:
        form = EditMemberForm(initial = {'key': 'value'})
    return render(request, 'teams/edit_member.html', {'form': form})

@login_required(login_url = reverse_lazy('login'))
def add_team(request):
    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/index.html', {'success': True})
    else:
        form = AddTeamForm(initial = {'key': 'value'})
    return render(request, 'teams/add_team.html', {'form': form})
