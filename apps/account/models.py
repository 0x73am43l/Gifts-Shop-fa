from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
from .usermanager import MyUserManager


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(blank=True, null=True)
    # phone_regex = RegexValidator(regex=r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', message="Phone number must be entered in the format: '09120001000'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=11, unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = []

    backend = 'apps.account.backend.ModelBackend'
