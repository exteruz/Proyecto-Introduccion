from django.views.generic import CreateView,ListView
from .models import user
from .forms import crearUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
class CrearUsuarioView(CreateView):
    model = user
    form_class = crearUsuario
    template_name = '../templates/registration/user_form.html'
    success_url = '/event/listview/'

class profileView(LoginRequiredMixin,ListView):
    model = user
    context_object_name = 'user'
    
    template_name = '../templates/profile.html'
# Create your views here.
