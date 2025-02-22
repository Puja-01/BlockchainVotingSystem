from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Voter
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


@api_view(['POST'])
def login_voter(request):
    username = request.data.get('username')
    password = request.data.get('password')

    User = get_user_model()  # Ensures compatibility with custom models
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.password):  # Manually check password
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


def home(request):
    return JsonResponse({"message": "Welcome to the Voting System API!"})

@api_view(['POST'])
def register_voter(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=400)

    if Voter.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    Voter.objects.create(username=username, password=make_password(password))
    return Response({"message": "Voter registered successfully!"}, status=201)

@api_view(['POST'])
def logout_voter(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"}, status=200)
    except Exception as e:
        return Response({"error": "Invalid token"}, status=400)