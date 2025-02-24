from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Voter, Election, Candidate, Vote
from .serializers import VoterSerializer, ElectionSerializer, CandidateSerializer, VoteSerializer

# ✅ Voter Registration
@api_view(['POST'])
def register_voter(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=400)

    if Voter.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    voter = Voter.objects.create(username=username, password=make_password(password))
    return Response({"message": "Voter registered successfully!", "voter_id": voter.id}, status=201)

# ✅ Voter Login
@api_view(['POST'])
def login_voter(request):
    username = request.data.get('username')
    password = request.data.get('password')

    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid password"}, status=400)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=400)

# ✅ Voter Logout
@api_view(['POST'])
def logout_voter(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"}, status=200)
    except Exception as e:
        return Response({"error": "Invalid token"}, status=400)

# ✅ CRUD Operations for Elections
class ElectionCreateView(generics.CreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can create elections

class ElectionListView(generics.ListAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

class ElectionRetrieveView(generics.RetrieveAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

class ElectionUpdateView(generics.UpdateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAdminUser]

class ElectionDeleteView(generics.DestroyAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAdminUser]

# ✅ CRUD Operations for Candidates
class CandidateCreateView(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAdminUser]

class CandidateListView(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateRetrieveView(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateUpdateView(generics.UpdateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAdminUser]

class CandidateDeleteView(generics.DestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAdminUser]

# ✅ Voting Process
class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can vote

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user)
