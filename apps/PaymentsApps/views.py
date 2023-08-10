from django.shortcuts import render
from django.views.generic import TemplateView,View

class CartView(TemplateView):

    template_name = "PaymentsApps/cart.html"
