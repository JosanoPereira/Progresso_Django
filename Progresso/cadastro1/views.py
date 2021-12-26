from django.db.models import fields
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Atividade, Campo, Status, Campus, Classe
from django.urls import reverse_lazy

# Create your views here.

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-atividade')

class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('inicio')

class CampusCreate(CreateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('inicio')

class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('inicio')

############## UPDATE ############## 
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-atividade')

############## DELETE ############## 
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastro1/form-excluir.html'
    success_url = reverse_lazy('listar-campo')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastro1/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')

############## LISTA ############## 
class CampoLista(ListView):
    model = Campo
    template_name = 'cadastro1/lista/campo.html'

class AtividadeLista(ListView):
    model = Atividade
    template_name = 'cadastro1/lista/atividade.html'