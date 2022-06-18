from django.urls import path
from .views import CrearUsuarioView,profileView

urlpatterns = [
    path('crearUsuario/', CrearUsuarioView.as_view() , name= "crearUsuario"),
    path('perfil/',profileView.as_view(),name="perfil")


]