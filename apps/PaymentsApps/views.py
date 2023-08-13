from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from apps.EventsApp.models import EventsModel
from apps.PaymentsApps.sesion_cart import Cart
from apps.PaymentsApps.models import OrderShop
from django.urls import reverse
from django.utils import timezone

class CartView(View):

    def get(self,request):
        cart = Cart(request)

        if cart.check():

            return render(request,"PaymentsApps/cart.html",{"cart":cart,"total_price":f"{cart.total():,}"})
        else:
            return render(request, "PaymentsApps/cart.html")

class AddToCartView(View):
    def post(self,request,pk):
        event=EventsModel.objects.get(id=pk)
        cart=Cart(request)
        cart.add(event,0)
        return redirect("PaymentsApp:Cart")

class DelFromCartView(View):

    def get(self,request,pk):
        event = EventsModel.objects.get(id=pk)
        cart = Cart(request)
        cart.del_item(event)
        return redirect("PaymentsApp:Cart")



class AddCartTOOrder(View):
    def post(self,request):
        cart=Cart(request)
        user=request.user
        if OrderShop.objects.filter(user=user,is_pay=False).exists():
            order=OrderShop.objects.get(user=user,is_pay=False)
            for item in cart:
                order.event.add(EventsModel.objects.get(id=item["id"]))
            # cart.remove(self.request)
            order.total_price=cart.total()
            order.save()
            return redirect(reverse("PaymentsApp:send-to-zarin", kwargs={"pk": order.id}))
        else:
            order = OrderShop.objects.create(user=user,total_price=cart.total())
            for item in cart:
                order.event.add(EventsModel.objects.get(id=item["id"]))
            # cart.remove(self.request)
            return redirect(reverse("PaymentsApp:send-to-zarin", kwargs={"pk":order.id}))


class SendToZarinpallView(View):

    def get(self,request,pk):
        order=OrderShop.objects.get(id=pk)

        if order.event.count()>0:
            return render(request, "PaymentsApps/cartPay.html", {"order": order, "cart": order})
        else:
            return render(request, "PaymentsApps/cartPay.html")

class DelFromOrder(View):

    def get(self,request,pk):

        cart=Cart(request)
        event=EventsModel.objects.get(id=pk)
        order=event.orderItem.get(is_pay=False,user=request.user)
        order.event.remove(event)
        cart.del_item(event)

        order.total_price=cart.total()
        order.save()
        return redirect("PaymentsApp:send-to-zarin",order.id)

import requests
import json
MERCHANT = "b3b73736-7999-4b64-b2e7-f14c42ee52a7"
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"

amount = 1000
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = '09011612090'
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'


class PayZarinPallView(View):

    def post(self,request,pk):

        order=OrderShop.objects.get(id=pk,user=request.user)
        request.session["order_id"]=order.id
        cart=Cart(request)
        cart.remove(self.request)

        if order.total_price != 0:
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.total_price,
                "callback_url": CallbackURL,
                "description": description,
                "metadata": {"mobile": order.user.phone}
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

        else:
            pass


class VerifyView(View):

    def get(self, request):
        t_status = request.GET.get('Status')
        order_id = request.session.get("order_id")
        order=OrderShop.objects.get(id=order_id)
        del request.session["order_id"]

        t_authority = request.GET['Authority']
        if request.GET.get('Status') == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": order.total_price,
                "authority": t_authority
            }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:
                    order.is_pay=True
                    order.pay_date(timezone.now())

                    for item in order.event.all():
                        event=item
                        event.users.add(request.user)
                        event.save()
                    order.save()

                    return redirect("/")

                #=============================================================

                elif t_status == 101:

                    return redirect("/")

                else:
                    return HttpResponse('Transaction failed.\nStatus: ' + str(
                        req.json()['data']['message']
                    ))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return redirect("/")

