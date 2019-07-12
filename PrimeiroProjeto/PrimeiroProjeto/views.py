from django.http import HttpResponse
from django.shortcuts import render

def hello(resquest):
    return render(resquest, 'index.html')

def artigos(request, ano):
    return HttpResponse("O ano enviado foi: " + str(ano))

def encontrarPessoa(nome):
    pessoas = [
        {'nome': 'Rômulo', 'idade': 19},
        {'nome': 'Ramon', 'idade': 20},
        {'nome': 'Caiena', 'idade': 18},
        {'nome': 'Victor', 'idade': 18},
    ]

    for pessoa in pessoas:
        if str(nome).lower() == pessoa['nome'].lower():
            return '{} encontradx, e tem {} anos'.format(pessoa['nome'], pessoa['idade'])
    else:
        return 'Pessoa não encontrada'

def pessoa(request, nome):
    result = encontrarPessoa(nome)
    return render(request, 'pessoa.html',{'result': result})
