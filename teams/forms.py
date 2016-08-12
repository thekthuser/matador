from django import forms
from teams.models import Member
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Member
        fields = ['username', 'phone', 'email']

    def save(self, commit=True):
        member = super(RegisterForm, self).save(commit=False)
        member.username = self.cleaned_data.get('username')
        member.email = self.cleaned_data.get('email')
        member.phone = self.cleaned_data.get('phone')
        member.connoisseur = False
        if commit:
            member.save()
        return member


