
 # -*- coding: latin-1 -*-
from django.shortcuts import render
from django.http import HttpResponse
from biblio.models import Libro
from django.views.generic import ListView, DetailView
from .models import Libro
from biblio.venta.models import Venta, VentaForm
from decimal import Decimal
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from carton.cart import Cart


# Create your views here.
def formulario_buscar(request):
    return render(request,'formulario_buscar.html')


def buscar(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
           error = True
        else:
          libros = Libro.objects.filter(titulo__icontains=q)
          return render(request, 'resultados.html', {'libros': libros, 'query': q})

    return render(request, 'index.html', {'error': error})


class IndexView(ListView):

    template_name = 'index.html'
    model = Libro


class LibroDetailView(DetailView):
    template_name = 'libro_detail.html'
    model= Libro


def gracias(request):
    return render(request,'gracias.html')

def ubicacion(request):
    return render(request,'ubicacion.html')

class lista_libros(ListView):
    template_name = 'libros.html'
    model=Libro



def catego(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
           error = True
        else:
          libros = Libro.objects.filter(categoria__icontains=q)
          return render(request, 'categoria.html', {'libros': libros, 'query': q})

    return render(request, 'formulario_buscar.html', {'error': error})






def add(request):
    cart = Cart(request.session)
    libro = Libro.objects.get(id=request.GET.get('id'))
    cart.add(libro, price=libro.precio)
    return render(request, 'gracias.html')


def remove(request):
    cart = Cart(request.session)
    libro = Libro.objects.get(id=request.GET.get('id'))
    cart.remove(libro)
    return render(request, 'show-cart.html')


class show(ListView):
    template_name = 'show-cart.html'
    model=Libro


def add_venta(request):
    cart = Cart(request.session)
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            new_venta = form.save()
            new_venta.total = cart.total
            new_venta.save()

            return render(request, 'exito.html')

    else:
        form = VentaForm()

    return render(request, 'show-cart.html', {'form': form})


class Ventas(ListView):
    template_name = 'resumen_ventas.html'
    model = Venta
