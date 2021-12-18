from django.urls import path
from .views import Blog

urlpatterns = [
    path('blog/', Blog, name='blog'),
]