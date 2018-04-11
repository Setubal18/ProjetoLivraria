from .models import Livro
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
# Create your views here.

# def Listar_Livros(request):
#     livro = Livro.objects.all()
#     livros = {'lista':livro}
#     return render(request,'livros_list.html',livros)

def listar_veiculo(request):
     query = request.GET.get("busca", '')
     page = request.GET.get('page', '')
     ordenar = request.GET.get("ordenar", '')
     if query:
         livro = Livro.objects.filter(modelo__icontains=query)
     else:
         try:
             if ordenar:
                 livro = Livro.objects.all().order_by(ordenar)
             else:
                 livro = Livro.objects.all()
             livro = Paginator(livro, 5)
             livro = livro.page(page)
         except PageNotAnInteger:
             livro = livro.page(1)
         except EmptyPage:
             livro = paginator.page(paginator.num_pages)
     livros = {'lista': livro}
     return render(request, 'livros_list.html', livros)

