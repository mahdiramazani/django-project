from django.urls import path
from . import views

app_name="charsoo"
urlpatterns=[
    path("",views.CharsooView.as_view(),name="CharsooView")
]