from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')

def Support(request):
    return render(request, 'support/support.html')

def Privacy(request):
    return render(request, 'support/privacy.html')

def Terms(request):
    return render(request, 'support/terms.html')

def Contact_Us(request):
    return render(request, 'support/contact_us.html')