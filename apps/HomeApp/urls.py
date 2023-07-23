from django.urls import path
from . import views

app_name="HomeApp"
urlpatterns=[
    path("",views.HomeAppView.as_view(),name="HomeApp"),
]