from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import GuildRoomModel,CommissionsModel
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


class ComisionListView(ListView):
    template_name = "GuildRoomApp/list_of_comision.html"
    model = CommissionsModel

    # def get_queryset(self):
    #     qs=super(ComisionListView, self).get_queryset()
    #
    #     return qs.filter(commissions_member=True)

class ComisionDetailView(DetailView):
    model = CommissionsModel
    template_name = "GuildRoomApp/comision_detail.html"
