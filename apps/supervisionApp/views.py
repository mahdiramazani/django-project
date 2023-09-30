from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Supervision


class AllSupervision(ListView):
    model =Supervision
    template_name = "supervisionApp/all-supervisionApp.html"


class DetailSupervision(DetailView,pk):
    model = Supervision
    template_name = "supervisionApp/supervision-detail.html"


