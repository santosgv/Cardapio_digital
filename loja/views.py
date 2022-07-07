from django.shortcuts import  render
from .models import Categoria , Produto

def home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()[:15]

    return render(request, 'home.html',{'categorias':categorias,
                                        'produtos': produtos,})


def categoria(request,id):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all().filter(categoria=id)
    return render(request,'produtos.html',{'categorias':categorias,
                                            'produtos':produtos })

def produto(request,id):
    categorias = Categoria.objects.all()
    produto = Produto.objects.get(id=id)

    return render(request,'produto.html',{ 'categorias':categorias,
                                            'produto':produto })