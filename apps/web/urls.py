from django.urls import path
from .views import (
    Home,
    Support,
    Privacy,
    Terms,
)

urlpatterns = [
    path('', Home, name='Home'),
    path('support/', Support, name='support'),
    path('privacy/', Privacy, name='privacy'),
    path('terms-and-conditions/', Terms, name='terms')
]