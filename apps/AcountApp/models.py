from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from django.utils import timezone
POST_CHOICES = (
    ("رئیس", "رئیس"),
    ("نائب رئیس اول", "نائب رئیس اول"),
    ("نائب رئیس دوم", "نائب رئیس دوم"),
    ("مدیراجرایی", "مدیر اجرایی"),
    ("خزانه دار", "خزانه دار"),
    ("کاربر عادی", "کاربر عادی"),
    ("عضو", "عضو"),
)
class UserManager(BaseUserManager):
    def create_user(self,phone, password=None):

        if not phone:
            raise ValueError("Users must have an phone Number")

        user = self.model(
            phone=phone,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,password=None):

        user = self.create_user(
            phone=phone,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone=models.CharField(max_length=12,
                           verbose_name="شماره تلفن",
                           unique=True)

    fullname=models.CharField(max_length=50,null=True,blank=True,verbose_name="نام و نام خانوادگی")
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )


    image=models.FileField(upload_to="users/images",null=True,blank=True,
                           verbose_name="عکس")
    is_publishing_news=models.BooleanField(default=False,verbose_name="اجازه ارسال اخبار دارد؟")
    guild_member=models.BooleanField(default=False,verbose_name="عضو اتحادیه")
    is_supervision=models.BooleanField(default=False,verbose_name="عضو نظارت و بازرسی")
    post = models.CharField(choices=POST_CHOICES,
                            null=True, blank=True,
                            max_length=50,
                            default="کاربر عادی",
                            verbose_name="سمت-مقام")
    is_active = models.BooleanField(default=True,verbose_name="کاربر فعال است؟")
    is_admin = models.BooleanField(default=False,verbose_name="ادمین وبسایت(به همه چیز دسترسی دارد)")
    commissions_member=models.BooleanField(default=False,
                                           verbose_name="عضو کمیسیون می باشد؟")
    board_of_directors=models.BooleanField(default=False,
                                           verbose_name="عضو هیئت رئیسه می باشد؟")
    created=models.DateTimeField(auto_now_add=True)
    bio=RichTextField(null=True,blank=True,
                      verbose_name="بیوگرافی")

    def __str__(self):

        return f"{self.fullname}"

    objects = UserManager()

    USERNAME_FIELD = "phone"


    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربرها"


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin,self.is_publishing_news


class OtpClass(models.Model):
    phone=models.CharField(max_length=14)
    fullname=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=60,blank=True)
    code=models.CharField(max_length=15)
    expiration_date=models.DateTimeField()

    def is_expiration_date(self):

        if self.expiration_date >= timezone.now():

            return True
        else:
            return False

    def __str__(self):

        return f"{self.phone}-{self.code}"


class PasswordResetTokenOtp(models.Model):
    phone=models.CharField(max_length=15)
    token=models.CharField(max_length=50)
    expiration_date = models.DateTimeField()


    def is_expiration_date(self):

        if self.expiration_date >= timezone.now():

            return True
        else:
            return False

