from django.forms import ModelForm
from .models import Pessoa

class PessoaFrom(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['primeiro_nome', 'ultimo_nome', 'idade', 'salario', 'foto']