from django.db import models
from apps.AcountApp.models import User
from apps.GuildRoomApp.models import GuildRoomModel
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=50)
    create=models.DateTimeField(auto_now_add=True)

class NewsModels(models.Model):
    writer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    writer_guild=models.ForeignKey(GuildRoomModel,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50)
    body=RichTextField()
    image=models.FileField(upload_to="image/news")
    slug=models.SlugField(allow_unicode=True,null=True,blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    view=models.IntegerField(default=0,null=True,blank=True)


    def save(self,*args,**kwargs):

        self.slug=slugify(self.title,allow_unicode=True)
        
        super(NewsModels, self).save(*args,**kwargs)

         
    def show_title(self):


        return self.body[:30]


    def __str__(self):

        return self.title

    def get_absolut_url(self):


        return reverse("NewsApp:detail_news",args=[self.slug])



