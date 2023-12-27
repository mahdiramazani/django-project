from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import CharsooModel

class CharsooView(View):

    def get(self,request):

        images=CharsooModel.objects.all()


        return render(request,"CharsooApp/standard.html",context={
            "images":images
        })


