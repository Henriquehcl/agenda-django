from django.urls import path

#from .views import ListaCompromissos

from . import views

urlpatterns = [
    # path('', ListaCompromissos.as_view(), name='home'),
    path('', views.listaCompromisso, name='index')
   
]
