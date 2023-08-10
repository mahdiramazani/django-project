from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View

class CartView(TemplateView):

    template_name = "PaymentsApps/cart.html"


class AddToCartView(View):

    def post(self,request):
        print("cart added")

        return redirect("PaymentsApp:Cart")

    def get(self,request):
        print("cart added")

        return redirect("PaymentsApp:Cart")
