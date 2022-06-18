from django.contrib import admin
from django.urls import path
from .views import eventList,eventCreateView,eventUpdateView,eventDeleteView,eventdetailview,eventCategorylist
from .views import ListCategoryView


urlpatterns = [
    path('listview/', eventList.as_view(), name= "listview"),
    path('crearEvento/', eventCreateView.as_view(),name='crearEvento'),
    path('actualizarEvento/<int:pk>',eventUpdateView.as_view(),name='actualizarEvento'),
    path('eliminarEvento/<int:pk>',eventDeleteView.as_view(),name='eliminarEvento'),
    path('verEvento/<str:pk>',eventdetailview.as_view(),name="verEvento"),
    path('eventoCategoria/<str:pk>', eventCategorylist.as_view(),name ="eventoCategoria"),
    path('filtro', ListCategoryView.as_view(), name = "filtro")

]