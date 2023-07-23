from django.shortcuts import render
from django.views.generic import TemplateView
from apps.NewsApp.models import NewsModels
from apps.GuildRoomApp.models import GuildRoomModel
from apps.AcountApp.models import User
class HomeAppView(TemplateView):

    template_name = "HomeApp/index.html"

    def get_context_data(self, **kwargs):
        context={}
        context["head_news"]=NewsModels.objects.all()[0:2]
        context["last_news"]=NewsModels.objects.last()
        context["body_news"]=NewsModels.objects.all()
        context["Guid"]=User.objects.filter(guild_member=True)


        return context
