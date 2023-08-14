from django.urls import path
from . import views

app_name="AboutUsApp"
urlpatterns=[
    path("",views.AboutView.as_view(),name="About")
]