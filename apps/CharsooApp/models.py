from django.db import models

class CharsooModel(models.Model):
    image=models.FileField(upload_to="charsoo/image",null=True,
                           blank=True,
                           verbose_name="تصویر")

    class Meta:
        verbose_name="سامانه چارسو"
        verbose_name_plural="سامانه چارسو"

