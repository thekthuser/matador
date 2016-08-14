from django import forms
from teams.models import Member, Team
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Member
        fields = ['username', 'phone', 'email']

    def save(self, commit=True):
        member = super(RegisterForm, self).save(commit=False)
        member.set_password(self.cleaned_data["password1"])
        member.username = self.cleaned_data.get('username')
        member.email = self.cleaned_data.get('email')
        member.phone = self.cleaned_data.get('phone')
        member.connoisseur = False

        testTeam = Team.objects.get(name='Team Valor')
        member.team = testTeam

        if commit:
            member.save()
        return member

class EditMemberForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Member
        fields = ['email', 'phone']

    #this is here so I can pass user from the view
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EditMemberForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        member = Member.objects.get(pk=self.user.id)
        member.email = self.cleaned_data.get('email')
        member.phone = self.cleaned_data.get('phone')

        if commit:
            member.save()
