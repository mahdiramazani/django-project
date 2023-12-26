from django.db import models
from jalali_date.utils import jalali_convert

class ViewHomeModels(models.Model):

    view=models.IntegerField()
    createdDate=models.DateTimeField(auto_now_add=True)


    def __str__(self):


        return f"{jalali_convert(self.createdDate)}-->{self.view}"


    class Meta:

        verbose_name="تعداد بازدید"
        verbose_name_plural="تعداد بازدید ها"


class ZarinpallClass(models.Model):

    link=models.TextField(
        verbose_name="لینک درگاه پرداخت"
    )


    class Meta:

        verbose_name="لینک درگاه پرداخت زرین پال"
        verbose_name_plural="لینک درگاه پرداخت زرین پال"

