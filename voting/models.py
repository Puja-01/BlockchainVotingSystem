from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL
from django.utils import timezone

class Voter(AbstractUser):
    has_voted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Voter"
        verbose_name_plural = "Voters"

class Election(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name="candidates")
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.election.name}"

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE, null=True, blank=True)  # Allow null for now
    timestamp = models.DateTimeField(default=timezone.now)


    class Meta:
        unique_together = ('voter', 'election')  # Ensures one vote per election per voter

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.name} in {self.election.name}"
