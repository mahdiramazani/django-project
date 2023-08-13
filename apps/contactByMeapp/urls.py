from django.urls import path
from . import views

app_name="ContactByMeappd"
urlpatterns=[
    path("",views.contactByMeView.as_view(),name="conatctByMeView"),
    path("lost-precious/",views.LostPreciousView.as_view(),name="Lost-Precious"),
    path("work-force/",views.WorkView.as_view(),name="work-force")
]