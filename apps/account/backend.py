from django.contrib.auth.backends import ModelBackend
from .models import MyUser


class PhoneBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        phone = kwargs['phone']
        try:
            user = MyUser.objects.get(phone=phone)
        except MyUser.DoesNotExist:
            pass
