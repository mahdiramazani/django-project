from django.urls import path
from . import views

app_name="PaymentsApp"
urlpatterns=[

  path("",views.CartView.as_view(),name="Cart"),
  path("add/<int:pk>",views.AddToCartView.as_view(),name="add-cart")
  ]