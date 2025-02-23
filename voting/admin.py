from django.contrib import admin

from django.contrib import admin
from .models import Election, Candidate, Vote, Voter

admin.site.register(Voter)
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)


# Register your models here.
