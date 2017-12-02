from django.conf.urls import  url
from .views import Home, ListaClientes, CriarCliente, DetalheClientes, ActualizarClientes
urlpatterns = [
    url(r'^lista/$', ListaClientes, name='lista'),
    url(r'^criar/$', CriarCliente, name='criar'),
    url(r'^(?P<id>\d+)/$', DetalheClientes, name='cliente_detalhe'),
    url(r'^(?P<id>\d+)/editar/$', ActualizarClientes, name='editar'),
]

