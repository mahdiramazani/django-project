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
    create=jmodels.jDateTimeField(auto_now_add=True)
    is_pay=models.BooleanField(default=False,
                               verbose_name="پرداخت شده؟")
    event = models.ManyToManyField(EventsModel,related_name="orderItem",
                              verbose_name="رویداد")
    total_price=models.IntegerField(verbose_name="قیمت")
    pay_date=models.DateTimeField(null=True,blank=True
    ,verbose_name="تاریخ پرداخت")


    class Meta:
        verbose_name="سبد خرید"
        verbose_name_plural="سبد های خرید"











