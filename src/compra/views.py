from django.shortcuts import render, get_object_or_404, redirect
from .forms import CompraForm
from django.http import HttpResponse, HttpResponseRedirect
from farmacia.utils import render_to_pdf
from estoque.models import Estoque
from .models import Compra
from .utils import calculacao


# Create your views here.


def Caixa(request):
    qs = Estoque.objects.all()
    # instance = get_object_or_404(Estoque, nome__iexact=produto)
    # if form.is_valid():
       
    #     resultado = calculacao(nome, quant, int(quantidade)) 
    #     instance.quantidade = resultado
    #     instance.save()

    #     print(nome + ' ' + produto + ' ' + str(resultado.calcular_valor(preco)) + ' ' + str(resultado.calcular_quantidade()))
    #     return redirect("home")

    #form = CompraForm(request.POST or None)
    # if form.is_valid():
    #     obj = Compra.objects.create(
    #     cliente = request.POST.get("nome"),
    #     produto = Estoque.objects.filter(id__iexact=request.POST.get("produto")),
    #     quantidade = request.POST.get("quantidade")
    #     )
    #     obj.save()
    #     print(cliente, produto)
    #     return redirect("lista")
    form = CompraForm(request.POST)

    if request.method == 'POST':
    
        cliente = request.POST.get("nome"),
        produto = request.POST.get("produto"),
        quantidade = request.POST.get("quantidade")
        # preco = instance.preco
        # quant = instance.quantidade
        # resultado = calculacao(instance.nome, instance.quantidade , int(quantidade)) 
        # instance.quantidade = resultado
        # instance.save()

        print(str(cliente) + '\n' + str(produto) + '\n'+ str(quantidade))
        return redirect("home")
    
    template = "compra.html"
    contexto = {'elementos': 'Caixa',
                'titulo': 'Kiame',
                'form': form,
                'object_item': qs,
        }
    return render(request, template, contexto) 

   



def Impressao(request, id=None):
    #qs = get_object_or_404(Estoque, id=id)
    #nome = request.POST.get("produto")
    #print(nome)
    qs = Estoque.objects.filter(id__iexact=id)
    template_name="impressao.html"
    contexto={'titulo':'Kiame',
                'elementos': 'produtos',
            'item': qs
    }
    pdf = render_to_pdf(template_name, contexto)
    return HttpResponse(pdf, content_type='application/pdf')
