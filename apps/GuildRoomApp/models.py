from django.db import models
from apps.AcountApp.models import User
from django.utils.text import slugify
from django.urls import reverse

class GuildRoomModel(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام اتحادیه")
    user=models.ManyToManyField(User,limit_choices_to={"guild_member":True},
    related_name="User"
    ,verbose_name="افراد")
    slug=models.SlugField(allow_unicode=True,null=True,blank=True)


    def save(self,**kwargs):
        self.slug=slugify(self.name,allow_unicode=True)

        super().save(**kwargs)

    def get_absolut_url(self):

        return reverse("GuildRoomApp:DetailGuild",args=[self.id])

    def __str__(self):


        return self.name

    class Meta:

        verbose_name="اتحادیه"
        verbose_name_plural="اتحادیه ها"


class CommissionsModel(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام کمیسون")
    user=models.ManyToManyField(User,limit_choices_to={"commissions_member":True},
    related_name="Comision"
    ,verbose_name="افراد")
    slug=models.SlugField(allow_unicode=True,null=True,blank=True)


    def save(self,**kwargs):
        self.slug=slugify(self.name,allow_unicode=True)

        super().save(**kwargs)

    def get_absolut_url(self):

        return reverse("GuildRoomApp:comision-detail",args=[self.id])

    def __str__(self):


        return self.name

    class Meta:

        verbose_name="کمیسیون"
        verbose_name_plural="کمیسیون ها"



