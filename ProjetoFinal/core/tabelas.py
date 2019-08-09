from django_tables2 import Table
from .models import Pessoa


class TabelaPessoa(Table):
    class Meta:
        model = Pessoa
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-striped table-bordered'}
        exclude = ('id',)
