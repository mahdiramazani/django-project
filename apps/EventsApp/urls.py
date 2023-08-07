from django.urls import path
from . import views

app_name="EventsApp"
urlpatterns=[
    path("",views.EventsView.as_view(),name="EventApp"),
    path("detail/",views.EventsView.as_view(),name="EventDetail")
]