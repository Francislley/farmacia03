from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic import ListView
from farmacia.utils import render_to_pdf
from .models import Estoque
from .forms import estoqueForm

# função de criação de produtos e armazenar no estoque

def Criar_Estoque(request):
    form = estoqueForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        
        instance.save()
        messages.success(request, "criado com sucesso!", extra_tags=" mt-2 alert alert-success")
        return HttpResponseRedirect("/estoque/lista/")
    # else:
    #     messages.error(request, "sem sucesso!", extra_tags=" mt-2 alert alert-danger")
        
    template_name="formulario_estoque.html"
    contexto = {    
                    'titulo':'Kiame',
                    'elementos': 'produtos',
                    'form': form,
    }
    return render(request, template_name, contexto)



def Estoque_apagar(request, id=None):
    instance = get_object_or_404(Estoque, id=id)
    if instance.delete(): 
        messages.success(request, "item eliminado!", extra_tags=" mt-2 alert alert-success")
    else:
        messages.error(request, "item eliminado!", extra_tags=" mt-2 alert alert-danger")
    return redirect("lista")
    
    

def Estoque_lista(request):
    qs = Estoque.objects.all()
    template_name="estoque_lista.html"
    query = request.GET.get("q")
    print(query)
    if query:
        qs = Estoque.objects.filter(Q(nome__icontains=query)|
                                    Q(tipo__icontains=query)
        )
   
    contexto={'titulo':'Kiame',
                'elementos': 'produtos',
            'object_item': qs
    }
    return render(request, template_name, contexto)




def Estoque_detalhe(request, id=None):
    
    instance = get_object_or_404(Estoque, id=id)
    #print(str(instance))
    template_name="estoque_detalhe.html"
    contexto={'titulo':'Kiame',
                'elementos': 'produtos',
                'obj': instance
    }
    return render(request, template_name, contexto)


def Estoque_alterar(request, id=None):
    
    instance = get_object_or_404(Estoque, id=id)
    form = estoqueForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item Alterado", extra_tags="mt-2 alert alert-success")
        return redirect("lista")
        
    template_name="Estoque_alterar.html"
    contexto={'titulo':'Kiame',
                'elementos': 'produtos',
                'instance': instance,
                'form': form
    }
    return render(request, template_name, contexto)




def Impressao(request, id=None):
    qs = get_object_or_404(Estoque, id=id)
    instance = Estoque
    #qs = Estoque.objects.filter(id__iexact='2')
    template_name="impressao.html"
    
    contexto={'titulo':'Kiame',
                'elementos': 'produtos',
            'item': qs
    }
    pdf = render_to_pdf(template_name, contexto)
    return HttpResponse(pdf, content_type='application/pdf')



class Armazenamento(View):
    def get(self, request, *args, **kwargs):
        template_name="armazenamento.html"
        contexto={'titulo':'Kiame',
                    'Armazenamento': 'Produtos Em Estoque',
                    'grafico': 'Grafico dos Produtos Armazenados'
        }
        
        return render(request,template_name, contexto)

# metodo do chart.js, permite visualizar o grafico de estoque
def get_data(request, *args, **kwargs):
    qs = Estoque.objects.all().count()
    qset = Estoque.objects.all()
    labels = []
    default_items = []
    for obj in qset:
        labels += [obj.nome]
        default_items += [obj.quantidade]
    data = {
        "labels": labels,
        "default": default_items,
    }
    return JsonResponse(data)
