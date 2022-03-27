from django.conf import settings
from random import randint
import ghasedakpack


def get_random_otp():
    return randint(100000, 999999)


def send_otp(phone, otp_rnd):
    sms = ghasedakpack.Ghasedak(settings.GHASEDAK_API)
    sms.verification({
        'linenumber': '300002525', 'receptor': phone, 'type': '1', 'template': 'Otp1', 'param1': otp_rnd
    })