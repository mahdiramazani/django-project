from django.db import models
from apps.AcountApp.models import User
from django.utils.text import slugify
from django.shortcuts import reverse

class Supervision(models.Model):
    name = models.CharField(max_length=50, verbose_name="نظارت و بازرسی")
    user = models.ManyToManyField(User, limit_choices_to={"is_supervision": True},
                                  related_name="Supervision"
                                  , verbose_name="افراد")
    slug = models.SlugField(allow_unicode=True, null=True, blank=True)

    def save(self, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)

        super().save(**kwargs)

    def get_absolut_url(self):
        return reverse("supervisionApp:detail-Supervision", args=[self.id])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نظارت و بازرسی"
        verbose_name_plural = "نظارت و بازرسی"