from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


POST_CHOICES = (
    ("رئیس", "رئیس"),
    ("نائب رئیس اول", "نائب رئیس اول"),
    ("نائب رئیس دوم", "نائب رئیس دوم"),
    ("مدیراجرایی", "مدیر اجرایی"),
    ("خزانه دار", "خزانه دار"),
    ("کاربر عادی", "کاربر عادی"),
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

    fullname=models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )


    image=models.FileField(upload_to="users/images",null=True,blank=True)
    is_publishing_news=models.BooleanField(default=False)
    guild_member=models.BooleanField(default=False)
    post = models.CharField(choices=POST_CHOICES,
                            null=True, blank=True,
                            max_length=50,
                            default="کاربر عادی",
                            verbose_name="سمت")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):

        return self.fullname

    objects = UserManager()

    USERNAME_FIELD = "phone"


    def __str__(self):
        return self.phone

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
        return self.is_admin
