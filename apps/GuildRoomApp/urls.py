from django.urls import path
from . import views

app_name="GuildRoomApp"
urlpatterns=[
        path("list/",views.UnionListView.as_view(),name="List"),
        path("detail/<int:pk>",views.UnionDetailVew.as_view(),name="DetailGuild"),
        path("member-of-guildroom",
             views.MemberOfUnionList.as_view()
             ,name="MemberOfUnionList"),
        path("comision-list/",views.ComisionListView.as_view(),name="Comision-list"),
        path("comision-detail/<int:pk>/",views.ComisionDetailView.as_view(),name="comision-detail")
]