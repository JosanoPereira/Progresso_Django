from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

class IndexModeloView(TemplateView):
    template_name = 'paginas/indexModelo.html'

class TelaCadastrarView(TemplateView):
    template_name = 'paginas/cadastrar.html'