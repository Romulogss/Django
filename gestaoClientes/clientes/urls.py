from django.urls import path
from .views import pessoas_list, criar, atualizar, delete

urlpatterns = [
    path('', pessoas_list, name='pessoas_list'),
    path('novo/', criar, name='novo'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('delete/<int:id>/', delete, name='delete'),
]
