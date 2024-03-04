from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tot_index(request):
  tots= Tot.objects.filter(user=request.user)
  return render(request, 'tots/index.html', { 'tots': tots })