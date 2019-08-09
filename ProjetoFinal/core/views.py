from django.shortcuts import render, redirect, get_object_or_404

from .forms import PessoaForm, VeiculoForm
from .models import (Pessoa, Veiculo, MovimentoRotativo,
                     Mensalista, MovimentoMensalista)
from .tabelas import TabelaPessoa
from django_tables2 import RequestConfig


# Create your views here.
def home(request):
    return render(request, 'core/index.html')


# CLeintes
def all_pessoas(request):
    # pessoas = Pessoa.objects.all()
    # return render(request, 'core/pessoas.html', {'pessoas': pessoas})
    tabela = TabelaPessoa(Pessoa.objects.all())
    RequestConfig(request).configure(tabela)
    return render(request, 'core/pessoas.html', {'pessoas': tabela})


def nova_pessoa(request):
    formulario = PessoaForm(request.POST or None)
    data = {'title': 'Novo Cliente', 'voltar': './', 'form': formulario}
    if formulario.is_valid():
        formulario.save()
        return redirect('core_pessoas')
    return render(request, 'core/form.html', data)


def delete_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    data = {'obj': pessoa, 'voltar': '../../', 'title': 'Excluir ' + pessoa.nome}
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_pessoas')
    return render(request, 'core/confirm-delete.html', data)


def update_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    formulario = PessoaForm(request.POST or None, instance=pessoa)
    data = {'form': formulario, 'voltar': '../../', 'title': 'Editar ' + pessoa.nome}
    if formulario.is_valid():
        formulario.save()
        return redirect('core_pessoas')
    return render(request, 'core/form.html', data)


# Veículos#
def all_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/veiculos.html', {'veiculos': veiculos})


def novo_veiculo(request):
    formulario = VeiculoForm(request.POST or None)
    data = {'title': 'Novo Veículo', 'voltar': './', 'form': formulario}
    if formulario.is_valid():
        formulario.save()
        return redirect('core_veiculos')
    return render(request, 'core/form.html', data)


def delete_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    data = {'obj': veiculo, 'voltar': '../../', 'title': 'Excluir ' + veiculo.placa + ' ' + veiculo.marca.nome}
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_veiculos')
    return render(request, 'core/confirm-delete.html', data)


def update_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    formulario = VeiculoForm(request.POST or None, instance=veiculo)
    data = {'form': formulario, 'voltar': '../../', 'title': 'Editar ' + veiculo.placa + ' ' + veiculo.marca.nome}
    if formulario.is_valid():
        formulario.save()
        return redirect('core_veiculos')
    return render(request, 'core/form.html', data)

#Mensalistas
def all_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/mensalistas.html', {'mensalistas': mensalistas})


def all_mov_mensalistas(request):
    movs_mensalistas = MovimentoMensalista.objects.all()
    return render(request, 'core/movs-mensalistas.html', {'movimentos': movs_mensalistas})


def all_mov_rotativos(request):
    movs_rotativos = MovimentoRotativo.objects.all()
    return render(request, 'core/movs-rotativos.html', {'movimentos': movs_rotativos})
