from django.shortcuts import render

def steam(requests):
    return render(requests, 'product/steam.html')