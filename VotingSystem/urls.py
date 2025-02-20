from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple home view
def home(request):
    return HttpResponse("Welcome to the Voting System")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('voting.urls')),  # Ensure your API routes work
    path('', home, name='home'),  # Add this line to fix the error
]

