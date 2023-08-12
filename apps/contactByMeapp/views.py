from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .  models import ContactUs


class contactByMeView(View):

    def post(self,request):

        subject=request.POST.get("subject")
        fullname=request.POST.get("fullname")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        body=request.POST.get("body")

        if subject and fullname and phone and body:
            ContactUs.objects.create(
                subject=subject,
                fullname=fullname,
                phone=phone,
                email=email,
                body=body
            )

            return redirect("ContactByMeappd:conatctByMeView")
        else:
            return redirect("ContactByMeappd:conatctByMeView")

    def get(self,request):

        return render(request,"ContactByMeapp/conatctbyme.html")


