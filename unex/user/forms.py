from .models import user
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class crearUsuario(UserCreationForm):
    class Meta:
        model = user
        fields = (
            'username',
        
            'pregrado',
            'email',
            'first_name',
            'last_name',
            'category',
            'pregrado',
            'faculty',
            'instagram',)