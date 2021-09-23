from django.shortcuts import render
from allauth.account.views import LoginView, SignupView
from allauth.account.forms import LoginForm

class LoginCustomView(LoginView):
    form_class = LoginForm
    template_name = "login.html"


class SignUpCustomView(SignupView):
    pass