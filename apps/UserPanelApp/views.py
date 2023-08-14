from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .forms import EditProfileForm
from django.urls import reverse
from apps.PaymentsApps.models import OrderShop
from apps.AcountApp.models import User
from django.contrib.auth import login
from .mixin import CheckLoginRequiredMixin

class UserPanelView(CheckLoginRequiredMixin,TemplateView):

    template_name = "UserPanelApp/profile.html"

class EditProfile(CheckLoginRequiredMixin,View):


    def post(self,request):

        form=EditProfileForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()

        return redirect(reverse("UserPanelApp:edit-panel"))


    def get(self,request):
        form=EditProfileForm(instance=request.user)

        return render(request,"UserPanelApp/edit-profile.html",{"form":form})



class OrderProfileView(CheckLoginRequiredMixin,View):

    def get(self,request):
        order=OrderShop.objects.filter(user=request.user)

        return render(request,"UserPanelApp/profile-order.html",{"order":order})

class OrderProfileDetail(CheckLoginRequiredMixin,View):

    def get(self,request,pk):
        order=OrderShop.objects.get(id=pk)

        return render(request,"UserPanelApp/order_detail.html",{"order":order})


class ChangePasswordView(CheckLoginRequiredMixin,View):

    def get(self,request):


        return render(request,"UserPanelApp/password-chanage.html")


    def post(self,request):

        oldpass=request.POST.get("oldpass")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        user=User.objects.get(phone=request.user.phone)
        context={
            "error":[]
        }

        if pass1 and pass2 and oldpass:

           if user.check_password(oldpass):

               if pass1 == pass2:

                   user.set_password(pass1)
                   user.save()
                   login(request, user)

                   return redirect("UserPanelApp:userpanel")

               else:
                   context["error"].append("پسورد ها با هم شباهت ندارند")
                   return render(request, "UserPanelApp/password-chanage.html",context)

           else:
               context["error"].append("پسورد قدیمی اشتباه است")
               return render(request, "UserPanelApp/password-chanage.html",context)

        return render(request,"UserPanelApp/password-chanage.html")






