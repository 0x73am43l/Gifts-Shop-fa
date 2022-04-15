from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from apps.account.models import MyUser
from django.urls import reverse
from unidecode import unidecode
from .forms import OtpPhoneInputForm
from .helper import get_random_otp, send_otp
from django.contrib import messages, auth
from requests import Response
from django.contrib.auth import update_session_auth_hash


def _session_id(request):
    session_id = request.session.session_key
    if not request.session.session_key:
        session_id = request.session.create()

        print(request.session.session_key)
    return session_id


@csrf_exempt
def user_signin(request):
    form = OtpPhoneInputForm()
    context = {
        "form": form
    }
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == "POST":
            try:
                if "phone" in request.POST:
                    phone = request.POST.get('phone')
                    phone = ("0" + str(unidecode(phone)))
                    user = MyUser.objects.get(phone=phone)
                    otp = get_random_otp()
                    # send_otp(phone, otp)
                    print(otp)
                    user.otp = otp
                    user.save()
                    request.session['phone_number'] = phone
                    return HttpResponseRedirect(reverse('otp_verify'))

            # TODO: Fix DoesNotExist MyUser
            except MyUser.DoesNotExist:
                form = OtpPhoneInputForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    otp = get_random_otp()
                    print(otp)
                    user.is_active = False
                    user.otp = otp
                    user.save()
                    request.session['phone_number'] = phone
                    return HttpResponseRedirect(reverse('otp_verify'))
        return render(request, 'account/signin.html', context)


# TODO: Fix User Verify
def user_verify(request):
    if request.user.is_authenticated:
        return redirect('Home')
    elif 'phone_number' not in request.session:
        return redirect('signin')
    else:
        # user = request.session.get('phone_number')
        user = MyUser.objects.get(phone=request.session.get('phone_number'))
        if request.method == "POST":
            # get_otp = int(request.POST.get('otp_nums'))
            # print(type(get_otp))
            # print(get_otp)
            # print(type(user.otp))
            if user.otp != int(request.POST.get('otp_nums')):
                print("Not Match OTP Code Sry!")
                return HttpResponseRedirect(reverse('otp_verify'))

            # otp_v = request.POST.get('otp_nums')
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('Home')
            return HttpResponseRedirect(reverse('Home'))
        # request.session.set_expiry(300)  # 5 min expire session
    return render(request, 'account/verify.html', {'user': user})


def user_logout(request):
    if request.session.has_key('phone_number'):
        del request.session['phone_number']

    logout(request)
    return redirect('Home')
