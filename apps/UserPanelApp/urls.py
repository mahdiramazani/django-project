from django.urls import path
from . import views

app_name="UserPanelApp"
urlpatterns=[
    path("",views.UserPanelView.as_view(),name="userpanel"),
    path("edit-profile/",views.EditProfile.as_view(),name="edit-panel"),
    path("profile-order/",views.OrderProfileView.as_view(),name="order-profile"),
    path("order/<int:pk>",views.OrderProfileDetail.as_view(),name="order-detail"),
    path("pass-change/",views.ChangePasswordView.as_view(),name="pass-change")
]