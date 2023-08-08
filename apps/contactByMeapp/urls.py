from django.urls import path
from . import views

app_name="ContactByMeappd"
urlpatterns=[
    path("",views.contactByMeView.as_view(),name="conatctByMeView")
]