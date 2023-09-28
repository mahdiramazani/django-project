from django.db import models
from apps.AcountApp.models import User
from apps.GuildRoomApp.models import GuildRoomModel
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
from django_jalali.db import models as jmodels

from jalali_date.utils import jalali_convert


class SliderModel(models.Model):
    image=models.FileField(upload_to="images/slider",verbose_name="تصویر")
    title=models.CharField(max_length=200,verbose_name="مقدمه")
    link=models.CharField(max_length=200,verbose_name="لینک")

    def __str__(self):

        return self.title

    class Meta:
        verbose_name="اسلایدر"
        verbose_name_plural="اسلایدرها"

class Category(models.Model):
    name=models.CharField(max_length=50,
                          verbose_name="نام دسته بندی")
    create=models.DateTimeField(auto_now_add=True,
                                verbose_name="تاریخ ایجاد")
    def __str__(self):

        return self.name
    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"



class NewsModels(models.Model):
    writer=models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             verbose_name="ادمین نویسنده")
    writer_guild=models.ForeignKey(GuildRoomModel,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True,
                                   verbose_name="اتحادیه مربوطه")
    title=models.CharField(max_length=50,
                           verbose_name="مقدمه")
    body=RichTextField(verbose_name="متن خبر")
    image=models.FileField(upload_to="image/news",verbose_name="عکس خبر")
    slug=models.SlugField(allow_unicode=True,
                          null=True,
                          blank=True,
                          verbose_name="اسلاگ:این قسمت پر نشود!")
    pub_date=models.DateTimeField(auto_now_add=True)
    view=models.IntegerField(default=0,
                             null=True,
                             blank=True,
                             verbose_name="تعداد بازدید")
    category=models.ManyToManyField(Category,
                                    related_name="category",
                                    verbose_name="دسته بندی ها")



    def save(self,*args,**kwargs):

        self.slug=slugify(self.title,allow_unicode=True)
        
        super(NewsModels, self).save(*args,**kwargs)

         
    def show_title(self):


        return f"{self.body[:50]}..."


    def __str__(self):

        return self.title

    def get_absolut_url(self):


        return reverse("NewsApp:detail_news",args=[self.id])

    def get_jalali_date(self):

        date=jalali_convert(self.pub_date)

        return date

    class Meta:
        verbose_name="خبر"
        verbose_name_plural="اخبار"


class Comment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="Comment",
                             verbose_name="کاربر")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.CharField(max_length=50,
                            verbose_name="متن کامنت")
    news=models.ForeignKey(NewsModels,
                           on_delete=models.CASCADE,
                           related_name="Comment",
                           verbose_name="اخبار مربوطه"
                           )
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.news.title[0:3]} --> {self.body[0:5]}"

    class Meta:
        verbose_name="کامنت"
        verbose_name_plural="کامنت ها"


class ImageGallery(models.Model):

    image=models.FileField(upload_to="imageGallery/image",
                           verbose_name="کاور تصویری")
    video=models.FileField(upload_to="imageGallery/video",
                           null=True,
                           blank=True,
                           verbose_name="ویدئو")
    title=models.CharField(max_length=150,
                           verbose_name="مقدمه")
    body = RichTextField(verbose_name="متن خبر")
    slug = models.SlugField(allow_unicode=True,
                            null=True,
                            blank=True,
                            verbose_name="اسلاگ:این قسمت پر نشود!")
    created=models.DateTimeField(auto_now_add=True)


    def save(self,**kwargs):

        self.slug=slugify(self.title,allow_unicode=True,)

        super().save(kwargs)


    def __str__(self):

        return self.title

    def get_absolut_url(self):


        return reverse("NewsApp:image_gallery",args=[self.id])

    def get_jalali_date(self):

        date=jalali_convert(self.created)

        return date

    class Meta:

        verbose_name="گالری تصویر"
        verbose_name_plural="گالری تصاویر"


