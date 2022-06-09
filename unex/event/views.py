from django.shortcuts import render
from django.views.generic import ListView
from .models import event


# Create your views here.
class eventList(ListView):
    model: event 
    template_name = "../templates/event_list.html"
    queryset = event.objects.all()
    
