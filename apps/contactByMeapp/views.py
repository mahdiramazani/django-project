from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .  models import ContactUs,LostPrecious,Work_Force


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



class LostPreciousView(View):

    def get(self,request):

        lost=LostPrecious.objects.filter(is_publish=True)

        return render(request,"ContactByMeapp/LostPrecious.html",{"lost":lost})


    def post(self,request):
        fullname=request.POST.get("fullname")
        phone=request.POST.get("phone")
        body=request.POST.get("body")

        if fullname and phone and body:
            LostPrecious.objects.create(fullname=fullname,
                                        phone=phone,
                                        body=body)

            return render(request, "ContactByMeapp/LostPrecious.html")

        return render(request,"ContactByMeapp/LostPrecious.html")


class WorkView(View):

    def get(self,request):

        work=Work_Force.objects.filter(is_publish=True)

        return render(request,"ContactByMeapp/work.html",{"work":work})


    def post(self,request):
        fullname=request.POST.get("fullname")
        phone=request.POST.get("phone")
        body=request.POST.get("body")
        number_register=request.POST.get("number_register")

        if fullname and phone and body:
            Work_Force.objects.create(fullname=fullname,
                                        phone=phone,
                                        body=body,
                                      number_register=number_register)

            return render(request, "ContactByMeapp/work.html")

        return render(request,"ContactByMeapp/work.html")