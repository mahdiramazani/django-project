from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import AboutClass

class AboutView(View):

    def get(self,request):
        object=AboutClass.objects.all().last()

        return render(request,"AboutUsApp/about.html",{"object":object})
