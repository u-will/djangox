from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Djangox
from django.urls import reverse_lazy

class DjangoxListView(ListView):
  template_name = "djangoxs/djangox-list.html"
  model = Djangox

class DjangoxDetailView (DetailView):
  template_name = "djangoxs/djangox-detail.html"
  model = Djangox       

class DjangoxUpdateView(UpdateView):
  template_name ="djangoxs/django-update.html"
  model = Djangox
  fields=['name', 'description']

class DjangoxDeleteView(DeleteView):
  template_name = 'djangoxs/djando-delete.html'
  model = Djangox
  success_url = reverse_lazy('djangox_list')

class DjangoxCreateView(CreateView): 
  template_name ='djangoxs/django-create.html'
  model = Djangox
  fields=['name', 'description']