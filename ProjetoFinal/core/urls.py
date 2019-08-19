from django.urls import path
from .urlsClass import (
    ClienteURL,
    VeiculoURL
)
from .views import (
    home,
    all_mov_rotativos,
    all_mov_mensalistas,
    all_mensalistas
)

urls = [
    path('', home, name='core_home'),
    ClienteURL.get_todos(),
    ClienteURL.update_pessoa(),
    ClienteURL.nova_pessoa(),
    ClienteURL.delete_pessoa(),
    VeiculoURL.get_todos(),
    VeiculoURL.novo_veiculo(),
    VeiculoURL.update_veiculo(),
    VeiculoURL.delete_veiculo(),
    path('mensalistas/', all_mensalistas, name='core_mensalistas'),
    path('movimentos-rotativos/', all_mov_rotativos, name='core_mov_rotativos'),
    path('movimentos-mensalistas/', all_mov_mensalistas, name='core_mov_mensalistas'),
]
