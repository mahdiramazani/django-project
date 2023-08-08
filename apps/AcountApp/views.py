from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View


class LoginView(TemplateView):
    template_name = "AcountApp/login.html"

class RegisterView(TemplateView):

    template_name = "AcountApp/register.html"


class UserDetailView(TemplateView):
    template_name = "AcountApp/userdetail.html"