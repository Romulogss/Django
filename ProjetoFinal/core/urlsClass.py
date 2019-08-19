from django.urls import path
from .views import (
    home,
    all_pessoas,
    nova_pessoa,
    delete_pessoa,
    update_pessoa,
    all_veiculos,
    novo_veiculo,
    delete_veiculo,
    update_veiculo,
    all_mov_rotativos,
    all_mov_mensalistas,
    all_mensalistas
)


class ClienteURL:

    @staticmethod
    def get_todos():
        return path('pessoas/', all_pessoas, name='core_pessoas')

    @staticmethod
    def nova_pessoa():
        return path('pessoas/nova', nova_pessoa, name='core_nova_pessoa')

    @staticmethod
    def update_pessoa():
        return path('pessoas/delete/<int:id>/', delete_pessoa, name='core_delete_pessoa')

    @staticmethod
    def delete_pessoa():
        return path('pessoas/update/<int:id>/', update_pessoa, name='core_update_pessoa')


class VeiculoURL:

    @staticmethod
    def get_todos():
        return path('veiculos/', all_veiculos, name='core_veiculos')

    @staticmethod
    def novo_veiculo():
        return path('veiculos/novo', novo_veiculo, name='core_novo_veiculo')
        path('veiculos/novo', novo_veiculo, name='core_novo_veiculo')

    @staticmethod
    def delete_veiculo():
        return path('veiculos/delete/<int:id>/', delete_veiculo, name='core_delete_veiculo')

    @staticmethod
    def update_veiculo():
        return path('veiculos/update/<int:id>/', update_veiculo, name='core_update_veiculo')
