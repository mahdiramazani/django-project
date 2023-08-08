from django.shortcuts import render
from django.views.generic import TemplateView

class contactByMeView(TemplateView):
    template_name = "ContactByMeapp/conatctbyme.html"
