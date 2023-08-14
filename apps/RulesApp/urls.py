from django.urls import path
from . import views

app_name="RulesApp"
urlpatterns=[
    path("",views.RulesView.as_view(),name="Rules"),
    path("detail/<int:pk>/",views.RulesDetail.as_view(),name="Rule-detail"),
    path("rule-senf/",views.RulesSenf.as_view(),name="rule-senf")
]