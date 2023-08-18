from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.NewsApp.models import NewsModels,ImageGallery,SliderModel
from apps.GuildRoomApp.models import GuildRoomModel
from apps.AcountApp.models import User
from .models import ViewHomeModels
from django.utils import timezone
from django.db.models import Q
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
        context["slider"]=SliderModel.objects.all()

        return context


class SearchView(View):

    def get(self,request):
        page = request.GET.get('page', 1)
        q=request.GET.get("q")
        query=NewsModels.objects.filter(
            Q(title__icontains=q) or Q(body__in=q)
        )
        paginator = Paginator(query, 1)
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return render(request,"HomeApp/search.html",{"object_list":object_list})


