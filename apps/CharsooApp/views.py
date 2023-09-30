from django.shortcuts import render
from django.views.generic import TemplateView


class CharsooView(TemplateView):

    template_name = "CharsooApp/standard.html"
