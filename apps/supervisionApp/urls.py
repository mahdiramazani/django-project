from django.urls import path
from . import views


app_name="supervisionApp"
urlpatterns=[
    path("list/",views.AllSupervision.as_view(),name="All-Supervision"),
    path("detail/<int:pk>/",views.DetailSupervision.as_view(),name="detail-Supervision")
]