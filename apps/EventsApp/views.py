from django.shortcuts import render
from django.views.generic import TemplateView

class EventsView(TemplateView):
    template_name = "EventsApp/events.html"
