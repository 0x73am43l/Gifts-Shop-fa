from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from .usermanager import MyUserManager
from django.db import models

phone_regex = RegexValidator(regex=r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}',
                             message="شماره همراه شما باید ۱۱ رقم و به این صورت باشد : 09120001200")


class MyUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True, blank=True, null=True, verbose_name='نام کاربری')
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="ایمیل")
    phone = models.CharField(validators=[phone_regex], max_length=11, unique=True, verbose_name="موبایل")
    otp = models.PositiveIntegerField(blank=True, null=True, verbose_name="کد OTP")
    otp_create_time = models.DateTimeField(auto_now=True, verbose_name="تاریخ ایجاد OTP")
    is_active = models.BooleanField(default=False, verbose_name='فعال')

    objects = MyUserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    backend = 'apps.account.backend.ModelBackend'

    class Meta:
        verbose_name_plural = '۱ - کاربر'
        verbose_name = ''


class Score(models.Model):
    User = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, verbose_name='کاربر')
    title = models.CharField(max_length=200, null=True, default='امتیاز دارد', verbose_name='عنوان')
    score = models.IntegerField(default=0, null=False, verbose_name="امتیاز")
    time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ دریافت امتیاز")

    def __str__(self):
        template = '{0.User} ({0.score}) {0.title}'
        return template.format(self)

    class Meta:
        verbose_name_plural = "۲ - امتیاز"
        verbose_name = ""


class UserProfile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ImageField()
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    purchases = models.IntegerField(default=0, verbose_name='خرید ها')

    class Meta:
        verbose_name_plural = 'پروفایل'


class UserVerifyDoc(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    # phone = models.ForeignKey(MyUser.phone, on_delete=models.CASCADE)
    home_phone = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(null=True)
    national_code = models.CharField(max_length=10, null=True)
    verify_code = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name_plural = 'وریفای مدارک'
        verbose_name = ''
