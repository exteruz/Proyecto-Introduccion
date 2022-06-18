from django.db import models


# Create your models here.
class event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, unique=True)
    Description = models.TextField(max_length=245)
    facultad = models.CharField(max_length=20, null=True, blank=True)
    undergrade = models.CharField(max_length=30,null=True,blank =True)
    image = models.ImageField(upload_to=  "../images",null= True,blank=True)
    place = models.CharField(max_length=200)
    points = models.IntegerField()
    date = models.DateTimeField()
    category = models.ManyToManyField('category')
    def __str__(self):
        return self.name
    class Meta:
         verbose_name = "event"
         ordering = ['name']
    

class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name
    class Meta:
         verbose_name = "category"
         ordering = ['name']
        
         
         
         
         
         
         
         

         



