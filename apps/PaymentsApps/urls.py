from django.urls import path
from . import views

app_name="PaymentsApp"
urlpatterns=[

  path("",views.CartView.as_view(),name="Cart"),
  path("add/<int:pk>",views.AddToCartView.as_view(),name="add-cart"),
  path("add-cart-to-order/",views.AddCartTOOrder.as_view(),name="add-cart-to-order"),
  path("del-item-from-order/<int:pk>",views.DelFromCartView.as_view(),name="del-item-from-order"),
  path("pay/<int:pk>",views.PayZarinPallView.as_view(),name="PayZarinPallView"),
  path("del-from-order/<int:pk>",views.DelFromOrder.as_view(),name="del-from-order"),
  path("paycart/<int:pk>",views.SendToZarinpallView.as_view(),name="send-to-zarin"),
  path("verify/",views.VerifyView.as_view(),name="verify")
  ]