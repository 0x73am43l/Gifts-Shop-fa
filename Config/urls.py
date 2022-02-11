"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from azbankgateways.urls import az_bank_gateways_urls

admin.site.site_header = 'داشبورد گیفتز شاپ'                    # default: "Django Administration"
admin.site.index_title = 'مدیریت'                 # default: "Site administration"
admin.site.site_title = 'داشبورد گیفتز شاپ'

urlpatterns = [
    path('panel/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('', include('apps.web.urls')),
    path('', include('apps.account.urls')),
    path('', include('apps.giftcard.urls')),
    path('', include('apps.payments.urls')),
    path('', include('apps.dashboard.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.cart.urls')),
]
