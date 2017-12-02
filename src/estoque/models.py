from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# class ProdutoProcurar(models.query.Queryset):
#     def procura(self, query):
#         return self.filter(nome__icontains=query)


# class ProdutoGerir(models.Manager):
#     def get_queryset(self):
#         return ProdutoProcurar(self.model, using=self._db)

#     def procura(self, query):
#         return self.get_queryset()
        




class Estoque(models.Model):
    nome                =   models.CharField(max_length=120, null=False)
    preco               =   models.FloatField(null=False)
    validade       		=   models.DateField(null=False )
    tipo                =   models.CharField(max_length=120, null=True)
    familia             =   models.CharField(max_length=120, null=True)
    quantidade          =   models.PositiveIntegerField(null=False)
    descricao           =   models.TextField(null=True)
    timestamp           =   models.DateTimeField(auto_now=False, auto_now_add=True)
    #objects             =   ProdutoGerir()
    def __str__(self):
        return self.nome

    #  def get_absolute_url(self):
    #     return reverse("detalhe", kwargs={"id": self.id})

    #metodo usado para eliminar um determinado item apartir do seu id
    def delete_url(self):
        return reverse("deletar", kwargs={"id": self.id})

    def edit_url(self):
        return reverse("alterar", kwargs={"id": self.id})

    def detail_url(self):
        return reverse("detalhe", kwargs={"id": self.id})
    
   