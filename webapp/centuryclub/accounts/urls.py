#from . import views
from django.urls import path, include
from .views import SignUpView


urlpatterns = [
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns = [
#   path('', views.index, name='index'),
   path("accounts/", include("django.contrib.auth.urls")),
   path("accounts/signup/", SignUpView.as_view(), name="signup"),

]
