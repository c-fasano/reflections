from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Memory


# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def about(request):
  return render(request, 'about.html')

def memories_index(request):
  memories = Memory.objects.all()
  return render(request, 'memories/index.html', { 'memories': memories })

def memories_detail(request, memory_id):
  memory = Memory.objects.get(id=memory_id)
  return render(request, 'memories/detial.html', { 'memory': memory })

class MemoryCreate(CreateView):
  model = Memory
  fields = ['name', 'location', 'date']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
