from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from apps.account.models import MyUser
from django.urls import reverse
import ghasedak


def user_signin(request):
    if request.method == "POST":
        if "phone" in request.POST:
            phone = request.POST.get('phone')
            user = MyUser.objects.get(phone=phone)
            login(request, user)
            return HttpResponseRedirect(reverse('Home'))

    return render(request, 'account/signin.html')


def user_logout(request):
    logout(request)
    return redirect('Home')
