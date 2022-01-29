from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from agendacore.models import Compromisso
from django.contrib import messages

@login_required(login_url='login/')
def meusCompromissos(request):
    usuario = request.user
    compromisso = Compromisso.objects.filter(usuario=usuario)
    response = {'compromissos': compromisso}
    return render(request, 'meuscompromissos.html', response)

def meuLogin(request):
    return render(request, 'login.html')

def autenticarLogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/meuscompromissos/')
        else:
            messages.error(request, 'Usuário ou Senha inválido!')
   
        return redirect('/meuscompromissos/')
        
def sairLogout(request):
    logout(request)
    return redirect('/')