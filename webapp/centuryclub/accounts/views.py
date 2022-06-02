from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import CustomUserCreationForm,CustomUserChangeForm


# Create your views here.
def index(request):
    return render(request, "accounts.html")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class EditView(CreateView):
    form_class = CustomUserChangeForm
    
    success_url = reverse_lazy("useredit")
    template_name = "registration/useredit.html"


def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})