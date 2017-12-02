from django.conf.urls import url
from .views import Estoque_lista, Criar_Estoque, Armazenamento, get_data, Estoque_detalhe, Estoque_alterar, Impressao, Estoque_apagar


urlpatterns = [
    url(r'^lista/$', Estoque_lista, name='lista'),
    url(r'^cadastramento/$', Criar_Estoque, name='cadastrar'),
    #url(r'^(?P<id>\d+)/impressao/$', Impressao, name='imprimir'),
    url(r'^armazenamento/$', Armazenamento.as_view(), name="armazenamento"),
    url(r'^(?P<id>\d+)/detalhe/$', Estoque_detalhe, name="detalhe"),
    url(r'^(?P<id>\d+)/alterar/$', Estoque_alterar, name="alterar"),
    url(r'^(?P<id>\d+)/apagar/$', Estoque_apagar, name="deletar"),
    #url(r'^(?P<id>\d+)/alterar/$', Estoque_detalhe, name="alterar"),

    url(r'^data/$', get_data, name="api-data"),
]

