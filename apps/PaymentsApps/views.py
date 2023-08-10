from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.EventsApp.models import EventsModel
from apps.PaymentsApps.sesion_cart import Cart

class CartView(View):

    def get(self,request):
        cart = Cart(request)

        return render(request,"PaymentsApps/cart.html",{"cart":cart})


class AddToCartView(View):

    def post(self,request,pk):
        event=EventsModel.objects.get(id=pk)

        cart=Cart(request)
        cart.add(event,0)



        return redirect("PaymentsApp:Cart")


