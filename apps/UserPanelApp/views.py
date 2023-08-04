from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .forms import EditProfileForm
from django.urls import reverse

class UserPanelView(TemplateView):

    template_name = "UserPanelApp/profile.html"

class EditProfile(View):


    def post(self,request):

        form=EditProfileForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()

        return redirect(reverse("UserPanelApp:edit-panel"))


    def get(self,request):
        form=EditProfileForm(instance=request.user)

        return render(request,"UserPanelApp/edit-profile.html",{"form":form})



