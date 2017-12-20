from django import forms
from .models import Club
from django.contrib.auth.models import User


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')


class ClubsForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


class PlayerSearchForm(forms.Form):
    name = forms.CharField(label="Wpisz nazwisko", max_length=62, empty_value=None)


class ClubSearchForm(forms.Form):
    name = forms.CharField(label="Wpisz nazwę klubu", max_length=62, empty_value=True)


class LoginForm(forms.Form):

    username = forms.CharField(max_length=150, label="nazwa użytkownika")
    password = forms.CharField(max_length=150, label="hasło", widget=forms.PasswordInput)


class SignupForm(forms.Form):

    username = forms.CharField(max_length=150, label="nazwa użytkownika")
    email = forms.CharField(max_length=150, label="adres email")
    password = forms.CharField(max_length=150, label="hasło", widget=forms.PasswordInput)
