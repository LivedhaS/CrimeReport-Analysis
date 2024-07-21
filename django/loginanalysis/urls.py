# myapp/urls.py

from django.urls import path
from .views import user_login, home

urlpatterns = [
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
]
