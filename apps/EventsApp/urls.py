from django.urls import path
from . import views

app_name="EventsApp"
urlpatterns=[
    path("",views.EventsView.as_view(),name="EventApp"),
    path("detail/<int:pk>",views.DetailEventView.as_view(),name="EventDetail"),
    path("event-list/",views.EventListView.as_view(),name="event-list")
]