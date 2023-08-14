from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
Category=(
    ("دستورالعمل های اجرایی","دستورالعمل های اجرایی"),
    ("آئین نامه اجرایی","آئین نامه اجرایی"),
    ("قانون نظام صنفی","قانون نظام صنفی"),
)

class RulesModel(models.Model):
    title=models.CharField(max_length=50,verbose_name="عنوان")
    category=models.CharField(choices=Category,max_length=30,verbose_name="دسته بندی")
    file=models.FileField(upload_to="rules/File",verbose_name="فایلpdf")
    text=RichTextField(verbose_name="متن قانون")

    def get_absolut_url(self):


        return reverse("RulesApp:Rule-detail",kwargs={"pk":self.id})

    def __str__(self):

        return self.title

    class Meta:

        verbose_name="قانون"
        verbose_name_plural="قوانین"
