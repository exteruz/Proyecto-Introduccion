from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import event
from .forms import eventform


# Create your views here.
class eventList(ListView):
    model: event 
    template_name = "../templates/event_list.html"
    queryset = event.objects.all()

class eventCreateView(CreateView):
    model = event
    form_class =  eventform
    template_name = '../templates/event_create.html'
    success_url = '../listview/'
    
class eventUpdateView(UpdateView):
    model = event
    form_class: eventform
    template_name = '../templates/event_create.html'
    success_url = '../listview/'

class eventDeleteView(DeleteView):
    model = event
    success_url = '../listview/'
    template_name = '../templates/event_confirm_delete.html'

class eventdetailview(DetailView):
    model=  event
    template_name = '../templates/event_detail.html'