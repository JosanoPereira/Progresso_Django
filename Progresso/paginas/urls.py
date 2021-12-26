from django.urls import path
from .views import IndexView, SobreView, TelaCadastrarView

urlpatterns = [
    #path('endereco', MinhaView.as_view(), name='nome da minhha url')
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    #path('modelo/', IndexModeloView.as_view(), name='preco'),
    path('cadastar/', TelaCadastrarView.as_view(), name='cadastar')
]