from tkinter import CASCADE
from django.db import models

# Create your models here.
class rango(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to=  "../images/icons",blank = True, null = True)
    def __str__(self):
            return self.name
    class Meta():
            verbose_name = "rango"
            ordering = ['name']
        
class insignia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=  "../images/icons",blank = True, null = True)
    def __str__(self):
            return self.name
    class Meta():
            verbose_name = "insignia"
            ordering = ['name']
    

class reward(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    puntos = models.IntegerField()
    image = models.ImageField(upload_to=  "../images/reward")
    rango = models.ForeignKey("rango",on_delete=models.CASCADE)
    class Meta():
        verbose_name = "reward"
        ordering = ['name']