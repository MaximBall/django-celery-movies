from django.shortcuts import render
from allauth.account.views import LoginView, SignupView
from allauth.account.forms import LoginForm, SignupForm
from django.views.generic import ListView
from payapp.models import Movie

class LoginCustomView(LoginView):
    form_class = LoginForm
    template_name = "login.html"


class SignUpCustomView(SignupView):
    form_class = SignupForm
    template_name = "sign_up.html"


class MoviesListView(ListView):
    model = Movie
    template_name = 'movies_list.html'




