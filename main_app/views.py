from django.shortcuts import render
from .models import Tot

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tot_index(request):
  tots= Tot.objects.all()
  return render(request, 'tots/index.html', { 'tots': tots })

def tot_detail(request, tot_id):
  tot = Tot.objects.get(id=tot_id)
  return render(request, 'tots/detail.html', { 'tot': tot })