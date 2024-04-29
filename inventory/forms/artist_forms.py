from django import forms
from django.forms import Form
from django.forms import CharField

class ArtistForm(Form):
   name = CharField(max_length=100, required = True)
   bio = CharField(max_length=500, widget=forms.Textarea(attrs=({'rows':5})), required = True)
   
   