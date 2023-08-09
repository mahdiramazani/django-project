from django.urls import path
from . import views
app_name="AcountApp"
urlpatterns=[

    path("login/",views.LoginView.as_view(),name="login"),
    path("register/",views.RegisterView.as_view(),name="register"),
    path("user-detail/",views.UserDetailView.as_view(),name="UserDetail"),
    path("otp/",views.OtpView.as_view(),name="OTP")
]