from django.db import models

# Create your models here.

class Pessoa(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    foto = models.ImageField(upload_to='clientes_fotos', null=True, blank=True)

    def __str__(self):
        return self.primeiro_nome + " " + self.ultimo_nome
