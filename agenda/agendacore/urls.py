from django.urls import path

#from .views import ListaCompromissos

from . import views
from meuscompromissos.views import detalhesCompromisso

urlpatterns = [
    # path('', ListaCompromissos.as_view(), name='home'),
    path('', views.listaCompromisso, name='index'),
    
   
]
