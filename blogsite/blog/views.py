from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, EntradaForm, BusquedaForm
from .models import Entrada

def index(request):
    entradas = Entrada.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/index.html', {'entradas': entradas})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntradaForm()
    return render(request, 'blog/crear_entrada.html', {'form': form})

def buscar(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            resultados = Entrada.objects.filter(titulo__icontains=termino)
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})


# Create your views here.
