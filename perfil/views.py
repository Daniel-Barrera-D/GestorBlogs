from django.shortcuts import render

#Models
from .models import Project 

# Create your views here.
def profile(request):

    projects = Project.objects.all()
    
    return render(request, 'profile.html', {'projects': projects})