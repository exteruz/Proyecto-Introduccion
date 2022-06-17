from django.urls import path
from .views import CrearUsuarioView

urlpatterns = [
    path('crearUsuario/', CrearUsuarioView.as_view() , name= "crearUsuario"),


]