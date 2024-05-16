from django.shortcuts import render
from .models import usuario

# Create your views here.


def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # exibir todos em uma nova página
    usuarios = {
        'usuarios': usuario.objetcs.all()
    }

    return render(request,'usuarios/usuarios.html', usuarios)