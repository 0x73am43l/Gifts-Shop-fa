from django.conf import settings
import ghasedakpack
import secrets
import string


# from random import randint


def get_random_otp():
    # return randint(100000, 999999)
    num = string.digits
    otp_num = ''.join(secrets.choice(num) for i in range(6))
    return otp_num


def send_otp(phone, otp_rnd):
    sms = ghasedakpack.Ghasedak(settings.GHASEDAK_API)
    sms.verification({
        'linenumber': '300002525', 'receptor': phone, 'type': '1', 'template': 'Otp1', 'param1': otp_rnd
    })
