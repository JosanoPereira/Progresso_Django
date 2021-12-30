from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .form import UsuarioForm
from django.urls import reverse_lazy
# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "cadastro1/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('loginView')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = "Registrar Usuário"
        context['titulo'] = "Registo de Usuários"
        return context