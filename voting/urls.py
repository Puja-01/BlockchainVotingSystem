from django.urls import path
from .views import (
    register_voter, login_voter, logout_voter,
    ElectionCreateView, ElectionListView, ElectionRetrieveView, ElectionUpdateView, ElectionDeleteView,
    CandidateCreateView, CandidateListView, CandidateRetrieveView, CandidateUpdateView, CandidateDeleteView,
    VoteCreateView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # ✅ Authentication Endpoints
    path('register/', register_voter, name='register'),
    path('login/', login_voter, name='login'),
    path('logout/', logout_voter, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    # ✅ Election Endpoints
    path('elections/', ElectionListView.as_view(), name='election-list'),
    path('elections/create/', ElectionCreateView.as_view(), name='election-create'),
    path('elections/<int:pk>/', ElectionRetrieveView.as_view(), name='election-detail'),
    path('elections/<int:pk>/update/', ElectionUpdateView.as_view(), name='election-update'),
    path('elections/<int:pk>/delete/', ElectionDeleteView.as_view(), name='election-delete'),

    # ✅ Candidate Endpoints
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('candidates/create/', CandidateCreateView.as_view(), name='candidate-create'),
    path('candidates/<int:pk>/', CandidateRetrieveView.as_view(), name='candidate-detail'),
    path('candidates/<int:pk>/update/', CandidateUpdateView.as_view(), name='candidate-update'),
    path('candidates/<int:pk>/delete/', CandidateDeleteView.as_view(), name='candidate-delete'),

    # ✅ Voting Endpoints
    path('vote/', VoteCreateView.as_view(), name='vote-create'),
from .views import cast_vote, get_votes  # Import the views handling blockchain API

urlpatterns = [
    path("vote/", cast_vote, name="cast_vote"),      # API to cast a vote
    path("get-votes/", get_votes, name="get_votes"),  # API to fetch votes
]
