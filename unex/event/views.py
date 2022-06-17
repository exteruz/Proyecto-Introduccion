from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import event,category
from .forms import eventform
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class eventList( LoginRequiredMixin, ListView):
    model: event 
    template_name = "../templates/event_list.html"
    queryset = event.objects.all()

class eventCategorylist(LoginRequiredMixin, ListView):
    model = event
    template_name = "../templates/event_list.html"
    #queryset =  event.objects.filter()

class eventCreateView(LoginRequiredMixin, CreateView):
    model = event
    form_class =  eventform
    template_name = '../templates/event_create.html'
    success_url = '../listview/'
    
class eventUpdateView(LoginRequiredMixin, UpdateView):
    model = event
    form_class = eventform
    template_name = '../templates/event_create.html'
    success_url = '../listview/'

class eventDeleteView(LoginRequiredMixin, DeleteView):
    model = event
    success_url = '../listview/'
    template_name = '../templates/event_confirm_delete.html'

class eventdetailview(LoginRequiredMixin, DetailView):
    model=  event
    template_name = '../templates/event_detail.html'