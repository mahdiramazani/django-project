from django.db import models
from ckeditor.fields import RichTextField
class AboutClass(models.Model):
    text=RichTextField(verbose_name="درباره ما:")


    def __str__(self):

        return self.text[0:10]


    class Meta:
        verbose_name="درباره ما"
        verbose_name_plural="درباره ما"
