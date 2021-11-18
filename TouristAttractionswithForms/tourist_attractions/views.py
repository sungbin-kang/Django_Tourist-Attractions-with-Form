from django.shortcuts import render, get_object_or_404
from .models import State, Attraction

def home(request):
  all_attractions = Attraction.objects.all()
  context = {"attractions" : all_attractions}
  return render(request, 'tourist_attractions/home.html', context)

def details(request, statename):
  attractions = Attraction.objects.all()
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'tourist_attractions/details.html', context)