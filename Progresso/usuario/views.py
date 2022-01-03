from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .form import UsuarioForm
from django.urls import reverse_lazy
from .models import Perfil


# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "cadastro1/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('loginView')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Docente")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = "Registrar Usuário"
        context['titulo'] = "Registo de Usuários"
        return context


class PerfilUpdate(UpdateView):
    template_name = "cadastro1/form.html"
    model = Perfil
    fields = ['nome_completo', 'bi', 'telefone']
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = "Editar Usuário"
        context['titulo'] = "Atualizar de Usuários"
        return context
