from django.shortcuts import render

#from django.shortcuts import redirect
#from django.contrib.auth import authenticate, login
#from django.contrib import messages
#from django.contrib.auth.forms import AuthenticationForm

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


# ###  Hmmmm this is not called ....
# def Login(request):
#     if request.method == 'POST':
  
#         # AuthenticationForm_can_also_be_used__
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             form = login(request, user)
#             messages.success(request, f' Welcome {username} !!')
#             return redirect('home')
#         else:
#             messages.info(request, f'account does not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'user/login.html', {'form':form, 'title':'log in'})


# when is this called ????
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = EditView(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = EditView()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)
