from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import GuildRoomModel


class UnionListView(ListView):

    template_name = "GuildRoomApp/List_of_unions.html"
    model = GuildRoomModel

class UnionDetailVew(DetailView):
    model = GuildRoomModel
    template_name = "GuildRoomApp/show_union.html"
