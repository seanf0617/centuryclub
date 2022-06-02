from . import views
from django.urls import path, include
from .views import SignUpView,EditView


urlpatterns = [
   path('', views.index, name='index'),
   path("accounts/", include("django.contrib.auth.urls")),
   path("accounts/signup/", SignUpView.as_view(), name="signup"),
   path("accounts/useredit/", EditView.as_view(), name="useredit"),

]
