from django.urls import path

#from .views import ListaCompromissos

from . import views

urlpatterns = [
    # path('', ListaCompromissos.as_view(), name='home'),
    path('', views.meusCompromissos),
    path('login/', views.meuLogin),
    path('login/submit', views.autenticarLogin),
    path('logout/', views.sairLogout),
    path('novocompromisso/', views.novoCompromisso),
    path('novocompromisso/cadastrar/', views.cadastrarCompromisso),
    path('deletar/<int:id_compromisso>/', views.deletar),    
    path('detalhes/', views.detalhesCompromisso),
    path('concluir/<int:id_compromisso>/', views.concluirCompromisso),
    path('concluidos/', views.compromissosConcluido),
    path('abertos/', views.compromissosAbertos),
    path('atrasados/', views.compromissosAtrasados),
     
    
]