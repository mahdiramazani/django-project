from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.AcountApp.models import User,OtpClass
from django.contrib.auth import login,logout,authenticate
import random
import requests
import ghasedakpack
sms = ghasedakpack.Ghasedak("8c1451922c0369b92a8da38aeb7d7b1e75db540b751dc9e30aa5abf61ad9dce7")


class LoginView(View):

    def get(self,request):

        return render(request,"AcountApp/login.html")

    def post(self,request):
        phone=request.POST.get("phone")
        password=request.POST.get("pass")

        if phone and password:
            if User.objects.filter(phone=phone).exists():
                user=authenticate(phone=phone,password=password)
                if user is not None:
                    login(request,user)

                    return redirect("/")
                else:
                    return render(request, "AcountApp/login.html",
                                  {"error": "کاربری با این مشخصات در سایت وجود ندارد"})
            else:
                return render(request,"AcountApp/login.html",
                              {"error":"کاربری با این مشخصات در سایت وجود ندارد"})

        return render(request,"AcountApp/login.html")

class RegisterView(View):

    def get(self,request):


        return render(request,"AcountApp/register.html")

    def post(self,request):

        fullname=request.POST.get("fullname")
        phone=request.POST.get("phone")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")

        if fullname and phone and pass2 and pass1:

            if User.objects.filter(phone=phone).exists():

                return render(request,"AcountApp/register.html",{"error":"حساب کاربری با این شماره در سایت وجود دارد!"})

            else:

                if pass2 != pass1:

                    return render(request,"AcountApp/register.html",{"error":"پسوردها با هم شباهت ندارند!"})
                else:
                    code=random.randint(1000,9999)
                    OtpClass.objects.create(phone=phone,code=code,
                                            fullname=fullname,password=pass2)

                    request.session["code"]=code
                    request.session["phone"]=phone

                    sms.verification(
                        {'receptor': phone,
                         'type': '1', 'template': 'TipHub',
                         'param1':code})

                    return redirect("AcountApp:OTP")

        return render(request,"AcountApp/register.html")


class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class OtpView(View):

    def get(self,request):
        phone = request.session.get("phone")

        return render(request,"AcountApp/otp.html",{"phone":phone})

    def post(self,request):
        context={
            "error":[]
        }

        phone = request.session.get("phone")
        code = str(request.session.get("code"))
        c_1=request.POST.get("c_1")
        c_2=request.POST.get("c_2")
        c_3=request.POST.get("c_3")
        c_4=request.POST.get("c_4")

        if c_1 and c_2 and c_3 and c_4:
            otpcode=c_1+c_2+c_3+c_4


            if OtpClass.objects.filter(phone=phone, code=code).exists():

                otp = OtpClass.objects.get(phone=phone)

                #check otp experition_date
                if otp.is_expiration_date():
                    if code == otpcode:

                        user=User.objects.create(fullname=otp.fullname,
                                                phone=otp.phone,
                                                password=otp.password)

                        user.set_password(otp.password)
                        user.save()
                        otp.delete()
                        return redirect("/")

                    else:
                        otp.delete()
                        context["error"].append("کد وارد شده صحیح نمی باشد!")

                        return render(request, "AcountApp/otp.html", context)
                else:
                    otp.delete()
                    context["error"].append("کد وارد شده منقضی شده است!")
                    return render(request, "AcountApp/otp.html",context)
            else:
                context["error"].append("کد وارد شده صحیح نمی باشد!")

                return render(request, "AcountApp/otp.html",context)

class UserDetailView(TemplateView):
    template_name = "AcountApp/userdetail.html"

