from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditUserProfileForm(UserChangeForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'place-holder': 'Enter your user name'}))
    
    class meta:
        model = User
        fields = ['username']
