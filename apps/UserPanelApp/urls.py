from django.urls import path
from . import views

app_name="UserPanelApp"
urlpatterns=[
    path("",views.UserPanelView.as_view(),name="userpanel"),
    path("edit-profile/",views.EditProfile.as_view(),name="edit-panel")
]