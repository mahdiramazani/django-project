from apps.EventsApp.models import EventsModel

class Cart:

    def __init__(self,request):

        self.session=request.session
        cart=self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def __iter__(self):

        cart=self.cart.copy()

        for item in cart.values():

            item["events"]=EventsModel.objects.get(id=int(item["id"]))
            item["total_price"]=int(item["count"]) * int(item["price"])

            yield item



    def total(self):
        cart=self.cart.copy()
        total=0
        for item in cart.values():
            total += item["price"]

        return total

    def check(self):

        if self.cart.items():
            return True

    def add(self,event,count):

        if event.id not in self.cart:
            self.cart[event.id]={
                "id":event.id,
                "title":event.title,
                "count":count,
                "price":event.price_event,
            }
            self.save()


    def remove(self,request):

        del request.session["cart"]

    def del_item(self,event):

        if str(event.id) in self.cart:
            del self.cart[str(event.id)]
            self.save()


    def save(self):
        self.session.modified = True




