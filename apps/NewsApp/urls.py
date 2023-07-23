from django.urls import path
from . import views

app_name="NewsApp"
urlpatterns=[
        path("detail/<str:slug>/",views.DetailNewsView.as_view(),name="detail_news")
]