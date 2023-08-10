from django.db import models
from apps.AcountApp.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from django_jalali.db import models as jmodels
CATEGORYEvent=(
    ("رویداد","رویداد"),
    ("همایش","همایش"),
    ("سمینار","سمینار"),
    ("جشنواره","جشنواره"),
    ("دوره آموزش","دوره آموزشی"),
)
HOW_TO_HOLD=(
    ("حضوری","حضوری"),
    ("آنلاین","آنلاین"),

)
class EventsModel(models.Model):
    title=models.CharField(max_length=50,
                           verbose_name="عنوان رویداد")
    short=models.TextField(
        verbose_name="خلاصه توضیحات رویداد"
    )
    body=RichTextField(verbose_name="توضیحات کلی رویداد")
    image=models.FileField(upload_to="images/events/",verbose_name="تصویر")
    categoryevent=models.CharField(max_length=100,
                                   choices=CATEGORYEvent,
                                   verbose_name="دسته بندی رویداد")
    price_event=models.IntegerField(default=0,
                                    verbose_name="هزینه رویداد(صفر به معنی رایگان بودن رویداد است)")
    how_to_hold=models.CharField(max_length=50,
                                 choices=HOW_TO_HOLD,
                                 default="حضوری",
                                 verbose_name="نحوه برگذاری")
    capacity=models.IntegerField(default=0,
                                 verbose_name="ظرفیت رودیداد(صفر به یعنی بدون محدودیت ظرفیت)")

    the_date_of_the_event=models.DateTimeField(verbose_name="تاریخ برگذاری رویداد")

    start_register=models.DateTimeField("تاریخ شروع ثبت نام در رویداد")
    end_of_register=models.DateTimeField("تاریخ پایان ثبت نام در رویداد")
    users=models.ManyToManyField(User,related_name="event_user",
                                 null=True,blank=True,
                                 verbose_name="کاربران رویداد")

    def is_can_register(self):
        if (self.end_of_register > self.start_register):

            if (self.capacity==0):
                return True
            elif (self.users.count()<self.capacity):
                return True
            else:
                return False

        return False

    def get_absolut_url(self):


        return reverse("EventsApp:EventDetail",kwargs={"id":self.id})



    def save(self,*args,**kwargs):

        return super(EventsModel,self).save(*args,**kwargs)

    class Meta:
        verbose_name="رویداد"
        verbose_name_plural="رویداد ها"

