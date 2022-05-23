from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=254)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "targetmiles", "location")
        labels = {'email':'email address',}
        labels = {'first_name':'First name',}
        labels = {'last_name':'Last name',}
        labels = {'location':'Location',}
        labels = {'targetmiles':'Target Miles',}
        # DOB


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "targetmiles", "location", )
        # location
        # DOB
