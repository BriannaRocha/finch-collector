from django.shortcuts import render
from .models import Tot

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tot_index(request):
  tots= Tot.objects.all()
  return render(request, 'tots/index.html', { 'tots': tots })