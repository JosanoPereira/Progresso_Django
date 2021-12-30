from django.db.models import fields
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Atividade, Campo, Status, Campus, Classe
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.

class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('loginView')
    group_required = u"ADM"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-campo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campos"
        context['botao'] = "Cadastrar"
        return context


class AtividadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('loginView')
    group_required = u"ADM"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-atividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Atividades"
        context['botao'] = "Cadastar"
        return context


class StatusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('loginView')
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('inicio')


class CampusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('loginView')
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('inicio')


class ClasseCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('loginView')
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('inicio')


############## UPDATE ##############
class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('loginView')
    group_required = u"ADM"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-campo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Edtitar Campo"
        context['botao'] = "Salvar"
        return context


class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('loginView')
    group_required = u"ADM"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastro1/form.html'
    success_url = reverse_lazy('listar-atividade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Edtitar Atividade"
        context['botao'] = "Salvar"
        return context


############## DELETE ##############
class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('loginView')
    group_required = u"ADM"
    model = Campo
    template_name = 'cadastro1/form-excluir.html'
    success_url = reverse_lazy('listar-campo')


class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('loginView')
    group_required = u"ADM"
    model = Atividade
    template_name = 'cadastro1/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')


############## LISTA ##############
class CampoLista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('loginView')
    model = Campo
    template_name = 'cadastro1/lista/campo.html'


class AtividadeLista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('loginView')
    model = Atividade
    template_name = 'cadastro1/lista/atividade.html'
