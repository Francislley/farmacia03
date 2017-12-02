from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from .forms import ClienteForm
from .models import Cliente
# Create your views here.
class Home(View):
    
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        contexto = {}
        return render(request, template_name, contexto)

def DetalheClientes(request, id):
    instance = get_object_or_404(Cliente, id=id)
    template_name = 'detalhes.html'
    contexto = {'obj':instance,
                'titulo': 'kiame'
            }
    return render(request, template_name, contexto)


def ActualizarClientes(request, id=None):
    instance = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        terminal = request.POST.get("terminal")
        morada = request.POST.get("morada")
        instance = Cliente.objects.filter(request).update(
            nome=nome, 
            terminal=terminal, 
            morada=morada
            )
        return HttpResponseRedirect("/cliente/lista/")

    template_name = 'formulario_cliente.html'
    contexto = {'obj':instance,
                'titulo': 'kiame'
    }
    return render(request, template_name, contexto)



def ListaClientes(request): 
    queryset_list = Cliente.objects.all() #.order_by("-id")
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset_list = paginator.page(paginator.num_pages)

    template_name = 'lista_clientes.html'
    contexto = {'object_item': queryset_list,
                'titulo': 'kiame'
                }
    return render(request, template_name, contexto)

'''class ListaClientes(View):
    qs = Cliente.objects.all()
    def get(self, request, *args, **kwargs):
        template_name = 'lista_clientes.html'
        contexto = {'object_item':self.qs}
        return render(request, template_name, contexto)
    ''' 

    
def CriarCliente(request): 

    if request.method == "POST":
        nome = request.POST.get("nome")
        terminal = request.POST.get("terminal")
        morada = request.POST.get("morada")
        instance = Cliente.objects.create(
            nome=nome, 
            terminal=terminal, 
            morada=morada
            )
        return HttpResponseRedirect("/cliente/lista/")

    template_name = 'formulario_cliente.html'

    contexto = {'titulo': 'kiame'}

    return render(request, template_name, contexto)

    