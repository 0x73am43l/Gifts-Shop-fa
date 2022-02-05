from django.urls import path
from .views import steam

urlpatterns = [
    path('item/steam', steam, name='steam'),
]