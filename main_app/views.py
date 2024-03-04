from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class TotCreate(CreateView):
  model = Tot
  fields = ['name', 'gender', 'age', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TotUpdate(UpdateView):
  model = Tot
  fields = ['age', 'gender', 'description']

class TotDelete(DeleteView):
  model = Tot
  success_url = '/tots/'