from django.contrib import admin

from .models import (Marca, Veiculo, Pessoa, MovimentoRotativo,
                     Mensalista, MovimentoMensalista)


# Register your models here.
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'entrada', 'saida', 'valor_hora', 'pago',
                    'horas_total', 'valor_total')

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = 'mensalista', 'data_pagamento', 'total'


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(MovimentoRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovimentoMensalista, MovMensalistaAdmin)
