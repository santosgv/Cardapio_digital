from django.shortcuts import redirect, render
from .models import Categoria , Produto

def home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'home.html',{'categorias':categorias,
                                        'produtos': produtos,})


def categoria(request,id):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all().filter(categoria=id)
    return render(request,'produto.html',{'categorias':categorias,
                                            'produtos':produtos })