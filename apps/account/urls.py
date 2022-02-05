from django.urls import path
from .views import user_signin, user_logout

urlpatterns = [
    path('signin/', user_signin, name='signin'),
    path('logout/', user_logout, name='logout'),
]
