from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Cliente(models.Model):
    nome       =   models.CharField(max_length=120, null=False)
    terminal   =   models.IntegerField()
    morada     =   models.CharField(max_length=120, null=False)
    timestamp  =   models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("cliente_detalhe", kwargs={"id": self.id})
        #return "/cliente/%d" %(self.id)