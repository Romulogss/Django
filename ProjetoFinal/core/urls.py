from django.urls import path

from .views import (home, all_pessoas, all_veiculos, all_mov_rotativos,
                    all_mov_mensalistas, all_mensalistas, nova_pessoa)

urls = [
    path('', home, name='core_home'),
    path('pessoas', all_pessoas, name='core_pessoas'),
    path('pessoas/nova', nova_pessoa, name='core_nova_pessoa'),
    path('veiculos', all_veiculos, name='core_veiculos'),
    path('movimentos-rotativos', all_mov_rotativos, name='core_mov_rotativos'),
    path('mensalistas', all_mensalistas, name='core_mensalistas'),
    path('movimentos-mensalistas', all_mov_mensalistas, name='core_mov_mensalistas'),
]
