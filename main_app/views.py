from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tot
from .forms import FeedingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tot_index(request):
  tots= Tot.objects.all()
  return render(request, 'tots/index.html', { 'tots': tots })

def tot_detail(request, tot_id):
  tot = Tot.objects.get(id=tot_id)
  feeding_form = FeedingForm()
  return render(request, 'tots/detail.html', {
    'tot': tot,
    'feeding_form': feeding_form
  })

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

def add_feeding(request, tot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.tot_id = tot_id
    new_feeding.save()
  return redirect('tot-detail', tot_id=tot_id)