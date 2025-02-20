from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Homepage route
]
from django.urls import path
from .views import register_voter

urlpatterns = [
    path('register/', register_voter, name="register"),
    path('register/', register_voter, name='register'),
]
