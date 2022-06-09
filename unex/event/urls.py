from django.contrib import admin
from django.urls import path
from .views import eventList

urlpatterns = [
    path('listview/', eventList.as_view(), name= "list_view"),
]