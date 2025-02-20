from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Voter
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate

@api_view(['POST'])
def login_voter(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        return Response({"message": "Login successful!"})
    else:
        return Response({"error": "Invalid credentials"}, status=400)
    

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


