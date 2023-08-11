from django.contrib import admin
from .models import OrderShop

@admin.register(OrderShop)
class OrderShopAdmin(admin.ModelAdmin):
    list_display = ("user","create","is_pay","total_price")
