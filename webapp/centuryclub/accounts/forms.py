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
        # Add DOB


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "targetmiles", "location", )
        # DOB

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
