from django.shortcuts import render
from .models import Project, Curriculum
# Create your views here.

def home(request):
    projects= Project.objects.all()
    curriculum= Curriculum.objects.first()

    return render(request, 'home.html', {'projects': projects, 'curriculum': curriculum})