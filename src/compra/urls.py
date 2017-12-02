from django.conf.urls import url
from .views import Impressao
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View


urlpatterns = [
    url(r'^(?P<id>\d+)/impressao/$', Impressao, name='imprimir'),
]
