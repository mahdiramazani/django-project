from django.shortcuts import render
from django.views.generic import TemplateView
from apps.NewsApp.models import NewsModels,ImageGallery
from apps.GuildRoomApp.models import GuildRoomModel
from apps.AcountApp.models import User
from .models import ViewHomeModels
from django.utils import timezone
import datetime
from datetime import date
class HomeAppView(TemplateView):

    template_name = "HomeApp/index.html"

    def get_context_data(self, **kwargs):

        if ViewHomeModels.objects.filter(
                createdDate__range=(timezone.now()-timezone.timedelta(days=1),timezone.now()+timezone.timedelta(days=20))).exists():



            ViewHomeModels.objects.create(view=0,createdDate=timezone.now())
        else:
            ViewHomeModels.objects.create(view=0,createdDate=timezone.now())


        context={}
        context["head_news"]=NewsModels.objects.all()[0:2]
        context["last_news"]=NewsModels.objects.last()
        context["body_news"]=NewsModels.objects.all()
        context["Guid"]=User.objects.filter(board_of_directors=True)
        context["Guild_news"]=NewsModels.objects.filter(writer=None)
        context["last_Guild_news"]=NewsModels.objects.filter(writer=None).last()
        context["last_image_gallery"]=ImageGallery.objects.all().last()
        context["image_gallery"] = ImageGallery.objects.all()
        context["must_view_news"]=NewsModels.objects.filter(view__gt=10)


        return context
