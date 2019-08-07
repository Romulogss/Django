from math import ceil

from django.db import models


# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=13)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    obs = models.TextField()
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca.nome + ' - ' + self.placa


# class Precos(models.Model):
#     rotativo = models.DecimalField()

class MovimentoRotativo(models.Model):
    entrada = models.DateTimeField(auto_now=False)
    saida = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        try:
            return ceil((self.saida - self.entrada).total_seconds() / 3600)
        except Exception:
            pass

    def valor_total(self):
        try:
            return self.valor_hora * self.horas_total()
        except Exception:
            pass
    def __str__(self):
        return self.veiculo.placa


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, models.CASCADE)
    inicio = models.DateField(auto_now=False)
    valor_mensal = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.veiculo.placa

class MovimentoMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, models.CASCADE)
    data_pagamento = models.DateField(auto_now=False)
    total = models.DecimalField(max_digits=6, decimal_places=2)
