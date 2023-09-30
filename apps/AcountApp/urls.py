from django.urls import path
from . import views
app_name="AcountApp"
urlpatterns=[

    path("login/",views.LoginView.as_view(),name="login"),
    path("register/",views.RegisterView.as_view(),name="register"),
    path("logout/",views.LogOutView.as_view(),name="LogOut"),
    path("forget-pass/",views.ForgetPassView.as_view(),name="forgetPass"),
    path("check-otc-forget-pass/",views.PassForgetOtp.as_view(),name="check-otc-forget-pass"),
    path("chnage-pass/",views.ChangePassView.as_view(),name="change-pass"),
    path("pass-change-complate/",views.PassChangeComplateView.as_view(),name="complate-pass-cjange"),
    path("user-detail/<int:pk>/",views.UserDetailView.as_view(),name="UserDetail"),
    path("otp/",views.OtpView.as_view(),name="OTP")
]