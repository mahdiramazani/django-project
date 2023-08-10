from apps.EventsApp.models import EventsModel

class Cart:

    def __init__(self,request):

        self.session=request.session
        cart=self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart


    def add(self,event):

        if event.id not in self.cart:
            self.cart[event.id]={
                "title":event.title,
                "count":0,
                "price":event.pice,
            }
        else:
            




