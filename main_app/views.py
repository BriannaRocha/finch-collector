from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tot, Toy
from .forms import FeedingForm

# Create your views here

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def tot_index(request):
  tots= Tot.objects.all()
  return render(request, 'tots/index.html', { 'tots': tots })

@login_required
def tot_detail(request, tot_id):
  tot = Tot.objects.get(id=tot_id)
  toys_tot_doesnt_have = Toy.objects.exclude(id__in = tot.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'tots/detail.html', {
    'tot': tot,
    'feeding_form': feeding_form,
    'toys': toys_tot_doesnt_have
  })

class TotCreate(LoginRequiredMixin, CreateView):
  model = Tot
  fields = ['name', 'gender', 'age', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TotUpdate(LoginRequiredMixin, UpdateView):
  model = Tot
  fields = ['age', 'gender', 'description']

class TotDelete(LoginRequiredMixin, DeleteView):
  model = Tot
  success_url = '/tots/'

@login_required
def add_feeding(request, tot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.tot_id = tot_id
    new_feeding.save()
  return redirect('tot-detail', tot_id=tot_id)

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, tot_id, toy_id):
  Tot.objects.get(id=tot_id).toys.add(toy_id)
  return redirect('tot-detail', tot_id=tot_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('tot-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)