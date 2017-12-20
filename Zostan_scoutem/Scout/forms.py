from django import forms
from .models import Club


class ClubsForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


class PlayerSearchForm(forms.Form):
    name = forms.CharField(label="Wpisz nazwisko", max_length=62, empty_value=None)


class ClubSearchForm(forms.Form):
    name = forms.CharField(label="Wpisz nazwę klubu", max_length=62, empty_value=True)