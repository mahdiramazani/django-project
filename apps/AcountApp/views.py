from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View


class LoginView(TemplateView):
    template_name = "AcountApp/login.html"

class RegisterView(View):

    def get(self,request):


        return render(request,"AcountApp/register.html")

    def post(self,request):


        return render(request,"AcountApp/register.html")

class OtpView(TemplateView):

    template_name = "AcountApp/otp.html"

class UserDetailView(TemplateView):
    template_name = "AcountApp/userdetail.html"

