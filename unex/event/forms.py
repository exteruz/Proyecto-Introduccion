from django import forms
from .models import event
from user.models import user
from django.contrib.admin import widgets

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'

class eventform(forms.ModelForm):
    points = forms.IntegerField(max_value=100, min_value = 0)
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    hour = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'time'}))
    class Meta:
        model = event
        fields = ['name','Description','facultad','image','place','points','category','hour','date']
       
         
       

   

   
  



    