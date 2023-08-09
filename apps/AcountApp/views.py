from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.AcountApp.models import User,OtpClass
import random
import requests
import ghasedakpack
sms = ghasedakpack.Ghasedak("8c1451922c0369b92a8da38aeb7d7b1e75db540b751dc9e30aa5abf61ad9dce7")


class LoginView(TemplateView):
    template_name = "AcountApp/login.html"

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
                    code=random.randint(9,9999)
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

class OtpView(View):

    def get(self,request):

        return render(request,"AcountApp/otp.html")

    def post(self,request):
        phone = request.session.get("phone")
        code = str(request.session.get("code"))
        otpcode=request.POST.get("code")

        print("code: ",code)
        print("code: ",phone)
        print("code: ",otpcode)
        print(code==code)

        if OtpClass.objects.filter(phone=phone, code=code).exists():
            print("test1")
            otp = OtpClass.objects.get(phone=phone)
            if code == otpcode:
                print("test2")

                user=User.objects.create(fullname=otp.fullname,
                                    phone=otp.phone,
                                         password=otp.password)

                user.set_password(otp.password)
                user.save()
                otp.delete()
                return redirect("/")
            return render(request, "AcountApp/otp.html")
        return render(request, "AcountApp/otp.html")

class UserDetailView(TemplateView):
    template_name = "AcountApp/userdetail.html"

