from django.urls import path
from .views import AtividadeCreate, CampoCreate, CampusCreate, ClasseCreate, StatusCreate
from .views import AtividadeDelete, CampoDelete
from .views import AtividadeUpdate, CampoUpdate
from .views import CampoLista, AtividadeLista

urlpatterns = [
    path('Cadastrar/campo', CampoCreate.as_view(), name='campo-cadastro'),
    path('Cadastrar/atividade', AtividadeCreate.as_view(), name='atividade-cadastro'),
    path('Cadastrar/status', StatusCreate.as_view(), name='status-cadastro'),
    path('Cadastrar/campus', CampusCreate.as_view(), name='campus-cadastro'),
    path('Cadastrar/classe', ClasseCreate.as_view(), name='classe-cadastro'),

    path('editar/campo/<int:pk>', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/campo/<int:pk>', CampoDelete.as_view(), name='excluir-campo'),

    path('listar/campo', CampoLista.as_view(), name='listar-campo'),
    path('listar/atividade', AtividadeLista.as_view(), name='listar-atividade'),
]
