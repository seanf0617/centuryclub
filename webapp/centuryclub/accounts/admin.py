from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "first_name", "last_name", "targetmiles", "location"]
    # DOB
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.site_header = "Century Club Database - Django Admin"
