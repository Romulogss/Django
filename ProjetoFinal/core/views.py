from django.shortcuts import render, redirect

from .forms import PessoaForm
from .models import (Pessoa, Veiculo, MovimentoRotativo,
                     Mensalista, MovimentoMensalista)


# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def all_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/pessoas.html', {'pessoas': pessoas})


def all_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/veiculos.html', {'veiculos': veiculos})


def all_mov_rotativos(request):
    movs_rotativos = MovimentoRotativo.objects.all()
    return render(request, 'core/movs-rotativos.html', {'movimentos': movs_rotativos})


def all_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/mensalistas.html', {'mensalistas': mensalistas})


def all_mov_mensalistas(request):
    movs_mensalistas = MovimentoMensalista.objects.all()
    return render(request, 'core/movs-mensalistas.html', {'movimentos': movs_mensalistas})


def nova_pessoa(request):
    formulario = PessoaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('core_pessoas')
    return render(request, 'core/form.html', {'form': formulario})

