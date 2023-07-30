from django.urls import path
from . import views

app_name="GuildRoomApp"
urlpatterns=[
        path("list/",views.UnionListView.as_view(),name="List"),
        path("detail/<int:pk>",views.UnionDetailVew.as_view(),name="DetailGuild"),
]