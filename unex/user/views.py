from django.shortcuts import render
from django.views.generic import CreateView
from .models import user
from .forms import crearUsuario
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
class CrearUsuarioView(CreateView):
    model = user
    form_class = crearUsuario
    template_name = '../templates/registration/user_form.html'
    success_url = '/event/listview/'


# Create your views here.
