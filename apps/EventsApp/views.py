from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView
from .models import  EventsModel
from django.utils import timezone

class EventsView(View):
    def get(self,request):
        context={
            "slider_page":EventsModel.objects.filter(end_of_register__gt=timezone.now()),
            "last_events":EventsModel.objects.filter(the_date_of_the_event__lt=timezone.now()),
            "future_events":EventsModel.objects.filter(the_date_of_the_event__gt= timezone.now())
        }

        return render(request,"EventsApp/events.html",context)


    def post(self,request):

        return render(request,"EventsApp/events.html")

class EventListView(ListView):
    template_name = "EventsApp/events-all.html"
    model = EventsModel
    paginate_by = 6

class DetailEventView(TemplateView):
    template_name = "EventsApp/eventDetail.html"
