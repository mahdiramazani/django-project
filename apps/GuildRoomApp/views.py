from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import GuildRoomModel
from apps.AcountApp.models import User

class UnionListView(ListView):

    template_name = "GuildRoomApp/List_of_unions.html"
    model = GuildRoomModel

class UnionDetailVew(DetailView):
    model = GuildRoomModel
    template_name = "GuildRoomApp/show_union.html"


class MemberOfUnionList(ListView):
    model = User
    template_name = "GuildRoomApp/listOfmemberUnion.html"

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.filter(board_of_directors=True)
