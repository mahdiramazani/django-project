from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import NewsModels

class DetailNewsView(DetailView):
    model = NewsModels
    template_name = "NewsApp/detail-news.html"



