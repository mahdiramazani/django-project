from django.urls import path
from . import views

app_name="NewsApp"
urlpatterns=[
        path("detail/<int:pk>/",views.DetailNewsView.as_view(),name="detail_news"),
        path("image_gallery/<int:pk>/",views.ImageGalleryView.as_view(),name="image_gallery"),
]