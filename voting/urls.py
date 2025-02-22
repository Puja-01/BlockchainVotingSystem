from django.urls import path
from .views import home, register_voter, login_voter, logout_voter
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_voter, name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('login/', login_voter, name='login'),
    path('logout/', logout_voter, name='logout'),  # Ensure this is included
]

