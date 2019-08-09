from django.urls import path

from .views import (home, all_pessoas, nova_pessoa,
                    delete_pessoa, update_pessoa,
                    all_veiculos, novo_veiculo,
                    delete_veiculo, update_veiculo,
                    all_mov_rotativos, all_mov_mensalistas,
                    all_mensalistas)

urls = [
    path('', home, name='core_home'),
    path('pessoas/', all_pessoas, name='core_pessoas'),
    path('pessoas/nova', nova_pessoa, name='core_nova_pessoa'),
    path('pessoas/delete/<int:id>/', delete_pessoa, name='core_delete_pessoa'),
    path('pessoas/update/<int:id>/', update_pessoa, name='core_update_pessoa'),
    path('veiculos/', all_veiculos, name='core_veiculos'),
    path('veiculos/novo', novo_veiculo, name='core_novo_veiculo'),
    path('veiculos/delete/<int:id>/', delete_veiculo, name='core_delete_veiculo'),
    path('veiculos/update/<int:id>/', update_veiculo, name='core_update_veiculo'),
    path('mensalistas/', all_mensalistas, name='core_mensalistas'),
    path('movimentos-rotativos/', all_mov_rotativos, name='core_mov_rotativos'),
    path('movimentos-mensalistas/', all_mov_mensalistas, name='core_mov_mensalistas'),
]
