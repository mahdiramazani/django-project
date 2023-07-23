from django.db import models
from apps.AcountApp.models import User



class GuildRoomModel(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام اتحادیه")
    user=models.ManyToManyField(User,limit_choices_to={"guild_member":True},
    related_name="User"
    ,verbose_name="افراد")



    def __str__(self):


        return self.name

    class Meta:

        verbose_name="اتاق اصناف"
        verbose_name_plural="اتاق اصناف"