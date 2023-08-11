from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.EventsApp.models import EventsModel
from apps.PaymentsApps.sesion_cart import Cart
from apps.PaymentsApps.models import OrderShop,OrderItem
from django.urls import reverse
class CartView(View):

    def get(self,request):
        cart = Cart(request)
        return render(request,"PaymentsApps/cart.html",{"cart":cart,"total_price":cart.total()})


class AddToCartView(View):
    def post(self,request,pk):
        event=EventsModel.objects.get(id=pk)
        cart=Cart(request)
        cart.add(event,0)
        return redirect("PaymentsApp:Cart")


class AddCartTOOrder(View):
    def post(self,request):
        cart=Cart(request)
        user=request.user
        if OrderShop.objects.filter(user=user,is_pay=False):
            order=OrderShop.objects.get(user=user,is_pay=False)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         event=EventsModel.objects.get(id=item["id"]),
                                         price=item["price"])
            return redirect(reverse("PaymentsApp:send-to-zarin", kwargs={"pk": order.id}))
        else:
            order = OrderShop.objects.create(user=user,total_price=cart.total())
            for item in cart:
                OrderItem.objects.create(order=order,
                                         event=EventsModel.objects.get(id=item["id"]),
                                         price=item["price"])

            return redirect(reverse("PaymentsApp:send-to-zarin", kwargs={"pk":order.id}))


class SendToZarinpallView(View):

    def get(self,request,pk):
        order=OrderShop.objects.get(id=pk)

        return render(request,"PaymentsApps/cartPay.html",{"order":order})

import requests
import json



MERCHANT = "b3b73736-7999-4b64-b2e7-f14c42ee52a7"
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"

amount = 1000
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = '09011612090'

CallbackURL = 'http://127.0.0.1:8080/verify/'


class PayZarinPallView(View):

    def post(self,request,pk):

        req_data = {
            "merchant_id": MERCHANT,
            "amount": 500000,
            "callback_url": CallbackURL,
            "description": description,
            "metadata": {"mobile": "09910765749"}
        }
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            return redirect(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")



