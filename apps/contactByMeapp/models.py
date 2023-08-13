from django.db import models

class ContactUs(models.Model):
    subject=models.CharField(max_length=50,verbose_name="موضوع")
    fullname=models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    phone=models.CharField(max_length=15,verbose_name="شماره تلفن")
    email=models.EmailField(null=True,blank=True,
                            verbose_name="ایمیل")
    body=models.TextField(verbose_name="متن پیام")

    class Meta:
        verbose_name="تماس با ما"
        verbose_name_plural="تماس با ما"
    def __str__(self):

        return f"{self.fullname}-{self.subject}"


class LostPrecious(models.Model):
    fullname=models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    phone=models.CharField(max_length=100,verbose_name="شماره تلفن")
    body=models.TextField(verbose_name="متن پیام")
    is_publish=models.BooleanField(default=False,verbose_name="منتشر شود؟")

    def __str__(self):

        return f"{self.fullname}-{self.phone}"

    class Meta:
        verbose_name="شی گمشده"
        verbose_name_plural="اشیا گمشده"




class Work_Force(models.Model):
    fullname=models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    phone=models.CharField(max_length=100,verbose_name="شماره تلفن")
    body=models.TextField(verbose_name="متن پیام")
    is_publish=models.BooleanField(default=False,verbose_name="منتشر شود؟")
    number_register=models.CharField(max_length=50,
                                     null=True,blank=True,
                                     verbose_name="شماره ثبت اتحادیه")

    def __str__(self):

        return f"{self.fullname}-{self.phone}"

    class Meta:
        verbose_name="نیروی کار"
        verbose_name_plural="نیروی کار"


