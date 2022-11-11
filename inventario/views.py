from itertools import product
from django.shortcuts import render, redirect
from inventario.models import Productos
from django.http import HttpResponse
from inventario.models import Productos

# Create your views here.

"""def busqueda_producto(request):
    mensaje = "<h1>Hola mundo</h1>"
    return HttpResponse(mensaje)"""

def busqueda_producto(request):
    return render(request, "search_products.html")  


def obtener_producto(request):
    producto = request.GET["prd"]
    return HttpResponse("El articulo buscado: %r" %producto)


def mostrar_productos(request):
    productos = Productos.objects.all()
    return render(request, "show_products.html", {'productos': productos})


def agregar_producto(request):
    if request.method == "POST":
        name = request.POST["nombre"]
        category = request.POST["categoria"]
        cost = request.POST["costo"]
        cantidad_stock = request.POST["stock"]
        description = request.POST["descripcion"]
        data = Productos(name=name, category=category, cost=cost, cantidad_stock=cantidad_stock, description=description)
        data.save()
        return redirect("/mostrar_productos/")
    else:
        return render(request, "add_products.html") 


def editar_producto(request, param):

    productos = Productos.objects.get(id=param)

    if request.method == "POST":
        productos.name = request.POST["nombre"]
        productos.category = request.POST["categoria"]
        productos.cost = request.POST["costo"]
        productos.cantidad_stock = request.POST["stock"]
        productos.description = request.POST["descripcion"]      
        productos.save()  
        return redirect("/mostrar_productos/")  
    else:
        return render(request, "edit_product.html",{'productos': productos}) 


def eliminar_producto(request, param):

    productos = Productos.objects.get(id=param)

    if request.method == "POST":        
        productos.delete()  
        return redirect("/mostrar_productos/")  
    else:
        return render(request, "delete_product.html",{'productos': productos})          