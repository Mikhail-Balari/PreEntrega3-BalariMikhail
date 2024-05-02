from django.shortcuts import render
from .forms import BusquedaForm
from .forms import ProductoForm
from .models import Producto

def buscar_producto(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            productos = Producto.objects.filter(nombre__icontains=termino)
            return render(request, 'resultados_busqueda.html', {'productos': productos})
    else:
        form = BusquedaForm()
    return render(request, 'buscar_producto.html', {'form': form})

def insertar_datos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'exito.html') 
    else:
        form = ProductoForm()
    return render(request, 'insertar_datos.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def resultados_busqueda(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET.get('q')
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'resultados_busqueda.html', {'productos': productos})