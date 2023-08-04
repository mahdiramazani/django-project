from django.shortcuts import render
from django.views.generic import TemplateView

class UserPanelView(TemplateView):

    template_name = "UserPanelApp/profile.html"

class EditProfile(TemplateView):
    template_name = "UserPanelApp/edit-profile.html"

