from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.AcountApp.models import User,OtpClass,PasswordResetTokenOtp
from django.contrib.auth import login,logout,authenticate
import random
import requests
import ghasedakpack
from .mixin import CheckLoginMixinMixin
sms = ghasedakpack.Ghasedak("091fd79dad29615b1b1ca22a91beac3c83db83baba36b25e28ef054650d7d71e")


class LoginView(CheckLoginMixinMixin,View):

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

class RegisterView(CheckLoginMixinMixin,View):

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
                                            fullname=fullname,password=pass2,expiration_date=timezone.now()+timezone.timedelta(minutes=5))

                    request.session["code"]=code
                    request.session["phone"]=phone

                    sms.verification(
                        {'receptor': phone,
                         'type': '1', 'template': 'registersms',
                         'param1':code})

                    return redirect("AcountApp:OTP")

        return render(request,"AcountApp/register.html")


class LogOutView(View):
    def get(self,request):

        if request.user.is_authenticated:

            logout(request)
            return redirect('/')

class ForgetPassView(CheckLoginMixinMixin,View):

    def post(self,request):
        phone=request.POST.get("phone")


        if User.objects.filter(phone=phone).exists():

            code=random.randint(1000,9999)
            OtpClass.objects.create(phone=phone,code=code,expiration_date=timezone.now()+timezone.timedelta(minutes=5))

            request.session["phone_forget"]=phone
            request.session["code_forget"]=code

            sms.verification(
                {'receptor': phone,
                 'type': '1', 'template': 'registersms',
                 'param1': code})

            return redirect("AcountApp:check-otc-forget-pass")

        return render(request,"AcountApp/forgetpass.html")

    def get(self,request):

        return render(request,"AcountApp/forgetpass.html")


class PassForgetOtp(CheckLoginMixinMixin,View):

    def get(self,request):
        phone = request.session.get("phone_forget")

        return render(request,"AcountApp/otpforgetpass.html",{"phone":phone})

    def post(self,request):
        context={
            "error":[]
        }
        phone = request.session.get("phone_forget")
        code = request.session.get("code_forget")



        c_1 = request.POST.get("c_1")
        c_2 = request.POST.get("c_2")
        c_3 = request.POST.get("c_3")
        c_4 = request.POST.get("c_4")

        if c_1 and c_2 and c_3 and c_4:
            otpcode = c_1 + c_2 + c_3 + c_4

            if OtpClass.objects.filter(phone=phone, code=code).exists():
                otp = OtpClass.objects.get(phone=phone, code=code)

                if otp.code == otpcode:

                    if otp.is_expiration_date():
                        code=random.randint(1000,9999)
                        OtpClass.objects.create(phone=otp.phone,code=code)
                        request.session["chnage_pass_code"]=code
                        request.session["chnage_pass_phone"]=otp.phone
                        otp.delete()

                        del request.session['phone_forget']
                        del request.session['code_forget']

                        return redirect("AcountApp:change-pass")


                    else:
                        otp.delete()
                        del request.session['phone_forget']
                        del request.session['code_forget']
                        context["error"].append("کد وارد شده فاقد اعتبار است")
                        return render(request, "AcountApp/otpforgetpass.html", context)
                else:
                    otp.delete()
                    context["error"].append("کد وارد شده فاقد اعتبار است")
                    del request.session['phone_forget']
                    del request.session['code_forget']
                    return render(request, "AcountApp/otpforgetpass.html", context)

            else:
                del request.session['phone_forget']
                del request.session['code_forget']
                context["error"].append("کد وارد شده اشتباه است")
                return render(request, "AcountApp/otpforgetpass.html",context)

        return render(request, "AcountApp/otpforgetpass.html")


class ChangePassView(CheckLoginMixinMixin,View):
    def get(self,request):

        return render(request,"AcountApp/changePass.html")

    def post(self,request):
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")

        if pass1 == pass2:
            code=request.session.get("chnage_pass_code")
            phone=request.session.get("chnage_pass_phone")

            del request.session['chnage_pass_code']
            del request.session['chnage_pass_phone']

            if OtpClass.objects.filter(phone=phone,code=code).exists():
                otc=OtpClass.objects.get(phone=phone,code=code)
                user=User.objects.get(phone=otc.phone)
                user.set_password(pass2)
                user.save()
                otc.delete()

                return redirect("AcountApp:complate-pass-cjange")


        else:
            pass

        return render(request,"AcountApp/changePass.html")


class PassChangeComplateView(CheckLoginMixinMixin,TemplateView):
    template_name = "AcountApp/complate_pass_change.html"

class OtpView(CheckLoginMixinMixin,View):

    def get(self,request):
        phone = request.session.get("phone")


        return render(request,"AcountApp/otp.html",{"phone":phone})

    def post(self,request):
        context={
            "error":[]
        }

        phone = request.session.get("phone")
        code = str(request.session.get("code"))

        del request.session['phone']
        del request.session['code']

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
                        login(request,user)
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

class UserDetailView(View):

    def get(self,request,pk):
        user=User.objects.get(id=pk)

        return render(request,"AcountApp/userdetail.html",{"user":user})


