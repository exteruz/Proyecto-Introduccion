from django.db import models
from django.contrib.auth.models import AbstractUser
from points.models import insignia,rango,reward
from event.models import category,event
class user(AbstractUser):
    pregrado = models.CharField(max_length=45,null=True, blank=True)
    faculty = models.CharField(max_length=35,null=True, blank=True)
    instagram = models.URLField(max_length=123, null=True, blank=True)
    insignia = models.ForeignKey(insignia, on_delete=models.CASCADE,  null=True, blank=True)
    rango = models.ForeignKey(rango, on_delete=models.CASCADE, null=True, blank=True)
    reward = models.ManyToManyField(reward,  blank=True)
    event = models.ManyToManyField(event, null=True, blank=True)
    category = models.ManyToManyField(category,  blank=True)
       
    



