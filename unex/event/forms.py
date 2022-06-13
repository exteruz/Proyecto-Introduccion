from dataclasses import field
from django import forms
from .models import event

class eventform(forms.ModelForm):
    class Meta:
        model = event
        fields = ['name','Description','facultad','image','place','points','date','category']

    