from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Voter(AbstractUser):
    has_voted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Voter"
        verbose_name_plural = "Voters"

class Election(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)  # Added description field
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255, blank=True, null=True)  # Added party field

    def __str__(self):
        return f"{self.name} - {self.election.name}"

class Vote(models.Model):
    voter = models.ForeignKey("Voter", on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE, default=1)  # Set default election ID
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.name} in {self.election.name}"
from django.db import models

# Create your models here.
