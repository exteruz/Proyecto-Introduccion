
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,TemplateView
from .models import event,category
from user.models import user
from .forms import eventform
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class eventList( LoginRequiredMixin, ListView):
    model = event 
    context_object_name = 'events'  # Default: object_list
    paginate_by = 4
    template_name = "../templates/event_list_test.html"
    queryset = event.objects.all()
    

class ListCategoryView(LoginRequiredMixin, ListView):
    model = event
    template_name = '../templates/event_list.html'
    def get_queryset(self):
        return event.objects.filter(id = self.request.user).values

class eventdetail(TemplateView):
        template_name = "../templates/event_list_test.html"
        




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
    def post(self,request,*argv,**kwargs):
        user_event = list(user.objects.values_list('category'))
        pk = request.POST.get('pk')
        for event in user_event:
            if event == pk:
                return super(eventUpdateView, self).post(request,*argv, **kwargs)
            else:
                return super(eventUpdateView, self).get(request)
    

class eventDeleteView(LoginRequiredMixin, DeleteView):
    model = event
    success_url = '../listview/'
    template_name = '../templates/event_confirm_delete.html'

class eventdetailview(LoginRequiredMixin, DetailView):
    model=  event

    template_name = "../templates/event_detail.html"