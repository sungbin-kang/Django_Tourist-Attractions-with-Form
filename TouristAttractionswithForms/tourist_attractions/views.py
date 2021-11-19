from django.shortcuts import render, get_object_or_404
from .models import State, Attraction
from .forms import StateForm, AttractionForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  all_attractions = Attraction.objects.all()
  context = {"attractions" : all_attractions}
  return render(request, 'tourist_attractions/home.html', context)

def details(request, statename):
  attractions = Attraction.objects.all()
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'tourist_attractions/details.html', context)

class StateCreate(CreateView):
  model = State
  template_name = "tourist_attractions/state_create_form.html"
  form_class = StateForm

class StateUpdate(UpdateView):
  model = State
  template_name = "tourist_attractions/state_update_form.html"
  form_class = StateForm

class StateDelete(DeleteView):
  model = State
  template_name = "tourist_attractions/state_delete_form.html"
  success_url = "/"
  

class AttractionCreate(CreateView):
  model = Attraction
  template_name = "tourist_attractions/attraction_create_form.html"
  form_class = AttractionForm

class AttractionUpdate(UpdateView):
  model = Attraction
  template_name = "tourist_attractions/attraction_update_form.html"
  form_class = AttractionForm

class AttractionDelete(DeleteView):
  model = Attraction
  template_name = "tourist_attractions/attraction_delete_form.html"
  success_url = "/"
  