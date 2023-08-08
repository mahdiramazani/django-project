from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView
from .models import NewsModels,Comment,ImageGallery
from django.urls import reverse

class DetailNewsView(DetailView):
    model = NewsModels
    template_name = "NewsApp/detail-news.html"

    def get_context_data(self,**kwargs):
        context = super(DetailNewsView, self).get_context_data(**kwargs)
        new=self.object
        new.view+=1
        new.save()

        context["related_news"]=NewsModels.objects.filter(category__in=self.object.category.all())\
            .exclude(id = self.object.id)
        context["last_news"]=NewsModels.objects.all().order_by("-pub_date").exclude(id = self.object.id)
        context["more_view"]=NewsModels.objects.filter(view__gt=10).exclude(id = self.object.id)
        return context

    def post(self,request,**kwargs):

        name=self.request.POST.get("name")
        email=self.request.POST.get("email")
        body=self.request.POST.get("body")
        object=NewsModels.objects.get(id=kwargs.get("id"))
        if email and name and body:

            Comment.objects.create(user=request.user,
                                   email=email,
                                   body=body,
                                   news=object)

        return redirect(reverse("NewsApp:detail_news",args=[kwargs.get("id")]))

class ImageGalleryView(DetailView):
    template_name = "NewsApp/detail-news.html"
    model=ImageGallery



class AllNewsView(TemplateView):

    template_name = "NewsApp/allNews.html"