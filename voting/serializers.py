from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Election, Candidate, Vote

User = get_user_model()

# Voter Serializer
class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Election Serializer
class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

# Candidate Serializer
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

# Vote Serializer
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
