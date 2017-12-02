from django.db import models
from clientes.models import Cliente
from estoque.models import Estoque
from django.core.urlresolvers import reverse
# Create your models here.


class Compra(models.Model):

    cliente     =   models.CharField(max_length=50)
    produto     =   models.CharField(max_length=100, null=False)
    quantidade  =   models.IntegerField()
    timestamp   =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.cliente

    def print_url(self):
        return reverse("imprimir", kwargs={"id": self.id})
    