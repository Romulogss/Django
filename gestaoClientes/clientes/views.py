from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PessoaFrom
# Create your views here.

@login_required
def pessoas_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa2.html', {'pessoas': pessoas})

@login_required
def criar(request):
    form = PessoaFrom(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('pessoas_list')
    return render(request, 'pessoa_form.html', {'formulario': form})

@login_required
def atualizar(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaFrom(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('pessoas_list')
    return render(request, 'pessoa_form.html', {'formulario': form})

@login_required
def delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PessoaFrom(request.POST or None, request.FILES or None, instance=pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoas_list')
    return render(request, 'pessoa_delete.html', {'formulario': form})