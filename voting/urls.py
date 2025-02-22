from django.urls import path
from .views import cast_vote, get_votes  # Import the views handling blockchain API

urlpatterns = [
    path("vote/", cast_vote, name="cast_vote"),      # API to cast a vote
    path("get-votes/", get_votes, name="get_votes"),  # API to fetch votes
]
