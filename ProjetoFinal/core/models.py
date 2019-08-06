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
