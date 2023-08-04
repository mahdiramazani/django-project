from django.db import models
from jalali_date.utils import jalali_convert
class ViewHomeModels(models.Model):

    view=models.IntegerField()
    createdDate=models.DateTimeField()


    def __str__(self):


        return f"{jalali_convert(self.createdDate)}-->{self.view}"


    class Meta:

        verbose_name="تعداد بازدید"
        verbose_name_plural="تعداد بازدید ها"