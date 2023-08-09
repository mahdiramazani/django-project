from django.db import models
from apps.AcountApp.models import User
from apps.EventsApp.models import EventsModel
from django.urls import reverse
from django_jalali.db import models as jmodels

class OrderShop(models.Model):
    user=models.ForeignKey(User,
                           on_delete=models.CASCADE,
                           related_name="orderShop",
                           verbose_name="کاربر")
    event=models.ManyToManyField(EventsModel,
                            related_name="ordershop",
                            verbose_name="رویداد مربوطه")
    create=jmodels.jDateTimeField(auto_now_add=True)
    is_pay=models.BooleanField(default=False,
                               verbose_name="پرداخت شده؟")
    price=models.IntegerField(verbose_name="قیمت")
    pay_date=jmodels.jDateTimeField(verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name="سبد خرید"
        verbose_name_plural="سبد های خرید"






