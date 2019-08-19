from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404
)
from django.contrib.auth.decorators import login_required
from .forms import (
    PessoaForm,
    VeiculoForm)
from .models import (
    Pessoa,
    Veiculo,
    MovimentoRotativo,
    Mensalista,
    MovimentoMensalista
)


# Create your views here.
@login_required
def home(request):
    return render(request, 'core/index.html')


# Cleintes
@login_required
def all_pessoas(request):
    pessoas = Pessoa.objects.all()
    formulario = PessoaForm()
    data = {'pessoas': pessoas, 'form': formulario}
    return render(request, 'core/pessoas.html', data)


@login_required
def nova_pessoa(request):
    formulario = PessoaForm(request.POST or None)
    data = {
        'title': 'Novo Cliente',
        'voltar': './',
        'form': formulario
    }
    if formulario.is_valid():
        formulario.save()
    return redirect('core_pessoas')


@login_required
def delete_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    data = {
        'obj': pessoa,
        'voltar': '../../',
        'title': 'Excluir ' + pessoa.nome
    }
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_pessoas')
    return render(request, 'core/confirm-delete.html', data)


@login_required
def update_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    formulario = PessoaForm(request.POST or None, instance=pessoa)
    data = {
        'form': formulario,
        'voltar': '../../',
        'title': 'Editar ' + pessoa.nome
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('core_pessoas')
    return render(request, 'core/form.html', data)


# Veículos
@login_required
def all_veiculos(request):
    veiculos = Veiculo.objects.all()
    formulario = VeiculoForm()
    data = {'veiculos': veiculos, 'form': formulario}
    return render(request, 'core/veiculos.html', data)


@login_required
def novo_veiculo(request):
    formulario = VeiculoForm(request.POST or None)
    data = {
        'title': 'Novo Veículo',
        'voltar': './',
        'form': formulario
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('core_veiculos')
    return render(request, 'core/form.html', data)


@login_required
def delete_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    data = {
        'obj': veiculo,
        'voltar': '../../',
        'title': 'Excluir ' + veiculo.placa + ' ' + veiculo.marca.nome
    }
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_veiculos')
    return render(request, 'core/confirm-delete.html', data)


@login_required
def update_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    formulario = VeiculoForm(request.POST or None, instance=veiculo)
    data = {
        'form': formulario,
        'voltar': '../../',
        'title': 'Editar ' + veiculo.placa + ' ' + veiculo.marca.nome
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('core_veiculos')
    return render(request, 'core/form.html', data)


# Mensalistas
@login_required
def all_mensalistas(request):
    mensalistas = get_list_or_404(Mensalista)
    return render(
        request,
        'core/mensalistas.html',
        {'mensalistas': mensalistas}
    )


@login_required
def all_mov_mensalistas(request):
    movs_mensalistas = get_list_or_404(MovimentoMensalista)
    return render(
        request,
        'core/movs-mensalistas.html',
        {'movimentos': movs_mensalistas}
    )


@login_required
def all_mov_rotativos(request):
    movs_rotativos = get_list_or_404(MovimentoRotativo)
    return render(
        request,
        'core/movs-rotativos.html',
        {'movimentos': movs_rotativos}
    )
