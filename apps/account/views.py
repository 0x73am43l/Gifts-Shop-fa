from random import randint
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from apps.account.models import MyUser
from django.contrib import messages
from django.urls import reverse
from unidecode import unidecode
from requests import Response
import ghasedakpack

def user_signin(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == "POST":
            try:
                if "phone" in request.POST:
                    phone = request.POST.get('phone')
                    phone = ("0" + str(unidecode(phone)))
                    user = MyUser.objects.get(phone=phone)
                    otp_rnd = randint(100000, 999999)
                    sms = ghasedakpack.Ghasedak(settings.GHASEDAK_API)
                    sms.verification({
                        'linenumber': '300002525', 'receptor': phone, 'type': '1', 'template': 'Otp1', 'param1': otp_rnd
                    })
                    print(otp_rnd)
                    MyUser.objects
                    MyUser.save(user)
                    # return redirect('otp_verify')
                return HttpResponseRedirect(reverse('otp_verify'))
            except MyUser.DoesNotExist:
                pass
                # user.is_active = False
                # user.otp = otp_rnd
                # MyUser.save()
                # return redirect('otp_verify')
            # else:
            #     messages.warning(request, 'شماره همراه وارد شده صحیح نمیباشد', 'warning')
                # return redirect('signin')
                # login(request, user)
                # return HttpResponseRedirect(reverse('Home'))

        return render(request, 'account/signin.html')


def user_verify(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == "POST":
            otp_v = request.POST.get('text')
            x = int(otp_v) == int(123456)
            print(otp_v)
            print(x)
    return render(request, 'account/verify.html')


def user_logout(request):
    logout(request)
    return redirect('Home')