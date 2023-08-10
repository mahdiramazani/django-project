from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.EventsApp.models import EventsModel
class CartView(TemplateView):

    template_name = "PaymentsApps/cart.html"


class AddToCartView(View):

    def post(self,request,pk):
        event=EventsModel.objects.get(id=pk)

        print(event.title)

        return redirect("PaymentsApp:Cart")


