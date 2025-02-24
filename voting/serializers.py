from rest_framework import serializers
from .models import Voter, Election, Candidate, Vote

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['id', 'username', 'email', 'has_voted']

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

    def validate(self, data):
        voter = data['voter']
        election = data['election']

        # Prevent duplicate voting
        if Vote.objects.filter(voter=voter, election=election).exists():
            raise serializers.ValidationError("You have already voted in this election.")

        return data
