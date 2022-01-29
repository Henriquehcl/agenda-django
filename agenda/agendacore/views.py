from django.http import response
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from agendacore.models import Compromisso
from django.contrib.auth.decorators import login_required


#class ListaCompromissos(TemplateView):
 #   template_name = 'compromisso.html'


def listaCompromisso(request):
    # return HttpResponse('teste de index')
    compromisso = Compromisso.objects.all()
    response = {'compromissos': compromisso}
    return render(request, 'compromisso.html', response)

#visualizar os compromissos, mas só se estiver logado
@login_required(login_url='/login/')
def meusCompromissos(request):
    pass

def loginUser(request):
    return render(request, 'login.html')