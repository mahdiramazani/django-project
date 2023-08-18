from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,DetailView
from .models import RulesModel

class RulesView(ListView):

    template_name = "RulesApp/Rules.html"
    model = RulesModel


class RulesDetail(DetailView):
    template_name = "RulesApp/rules-detail.html"
    model = RulesModel

class RulesSenf(ListView):
    template_name = "RulesApp/rule_senf.html"
    model = RulesModel

    def get_queryset(self):
        qs=super().get_queryset()

        return qs.filter(category="قانون نظام صنفی")

class InstructionsViews(ListView):
    template_name = "RulesApp/instructions.html"
    model = RulesModel

    def get_queryset(self):
        qs=super().get_queryset()

        return qs.filter(category="دستورالعمل های اجرایی")

class RegulationsViews(ListView):
    template_name = "RulesApp/regulations.html"
    model = RulesModel

    def get_queryset(self):
        qs=super().get_queryset()

        return qs.filter(category="آئین نامه اجرایی")