from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appinventario.models import *
from appinventario.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def inicio(request):
    return render(request, 'appinventario/inicio.html')

def productos(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto( idproducto=informacion['idproducto'],  nombreproducto=informacion['nombreproducto'], 
            tipo=informacion['tipo'], precio=informacion['precio'],existencias=informacion['existencias'], idbodega=informacion['idbodega'],
            idproveedor=informacion['idproveedor'])
            producto.save()
            return render(request, "appinventario/inicio.html")
    else:
            miFormulario = ProductoFormulario()
    return render(request, 'appinventario/productos.html')


def bodegas(request):
    return render(request, 'appinventario/bodegas.html')

def leerbodega(request):
    bodegas = Bodega.objects.all()
    contexto = {"bodegas": bodegas}
    return render(request, "appinventario/leerbodega.html", contexto)

def eliminarbodega(request, bodega_nombrebodega):
    bodega = Bodega.objects.get(nombrebodega=bodega_nombrebodega)
    bodega.delete()
    
    bodega = Bodega.objects.all()
    contexto= {"bodegas":bodegas}
    return render(request, "appinventario/leerbodega.html", contexto)

def editarbodega(request, bodega_nombrebodega):
    bodega = Bodega.objects.get(nombrebodega=bodega_nombrebodega)
    if request.method == 'POST':
        miFormulario = BodegaFormulario(request.POST)
       
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            bodega.idbodega= informacion['idbodega']
            bodega.nombrebodega = informacion['nombrebodega']
            bodega.ubicacion = informacion['ubicacion']
            bodega.save()
            
            return render(request, "appinventario/editarbodega.html")
        
    else:
        miFormulario = BodegaFormulario(initial={ 'idbodega':bodega.idbodega,
                                                  'nombrebodega' : bodega.nombrebodega,
                                                  'ubicacion':bodega.ubicacion                                                                                                 
                                                   })
        
    return render(request, "appinventario/editarbodega.html", {"miFormulario":miFormulario, "bodega_nombrebodega":bodega_nombrebodega})   

def proveedores(request):
    return render(request, 'appinventario/proveedores.html')



def leerproveedor(request):
    proveedores = Proveedor.objects.all()
    contexto = {"proveedores": proveedores}
    return render(request, "appinventario/leerproveedor.html", contexto)

def eliminarproveedor(request, proveedor_empresa):
    proveedor = Proveedor.objects.get(empresa=proveedor_empresa)
    proveedor.delete()
    
    proveedor = Proveedor.objects.all()
    contexto= {"proveedores":proveedores}
    return render(request, "appinventario/leerproveedor.html", contexto)

def editarproveedor(request, proveedor_empresa):
    proveedor = Proveedor.objects.get(empresa=proveedor_empresa)
    if request.method == 'POST':
        miFormulario = ProveedorFormulario(request.POST)
       
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proveedor.idproveedor = informacion['idproveedor']
            proveedor.empresa = informacion['empresa']
            proveedor.actividad= informacion['actividad']
            proveedor.email=informacion['email']
            proveedor.contacto=informacion['contacto']
            proveedor.save()
            
            return render(request, "appinventario/inicio.html")
        
    else:
        miFormulario = ProveedorFormulario(initial={ 'idproveedor':proveedor.idproveedor,
                                                     'empresa' : proveedor.empresa,
                                                     'actividad':proveedor.actividad ,      
                                                     'email' : proveedor.email,
                                                     'contacto' : proveedor.contacto                                                                                                    
                                                   })
        
    return render(request, "appinventario/editarproveedor.html", {"miFormulario":miFormulario, "proveedor_empresa":proveedor_empresa})        



def leerproducto(request):
    productos = Producto.objects.all()
    contexto = {"productos": productos}
    return render(request, "appinventario/leerproducto.html", contexto)


def eliminarproducto(request, producto_nombreproducto):
    producto = Producto.objects.get(nombreproducto=producto_nombreproducto)
    producto.delete()
    
    producto = Producto.objects.all()
    contexto= {"productos":productos}
    return render(request, "appinventario/leerproducto.html", contexto)


def editarproducto(request, producto_nombreproducto):
    producto = Producto.objects.get(nombreproducto=producto_nombreproducto)
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
       
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            producto.idproducto = informacion['idproducto']
            producto.nombreproducto = informacion['nombreproducto']
            producto.tipo=informacion['tipo']
            producto.precio = informacion['precio'] 
            producto.existencias = informacion['existencias']
            producto.idbodega = informacion['idbodega']
            producto.idproveedor = informacion['idproveedor']
            
            producto.save()
            
            return render(request, "appinventario/leerproducto.html")
        
    else:
        miFormulario = ProductoFormulario(initial={  'idproducto':producto.idproducto,
                                                     'nombreproducto' : producto.nombreproducto,
                                                     'tipo':producto.tipo ,      
                                                     'precio': producto.precio,
                                                     'existencias' : producto.existencias,
                                                     'idbodega' : producto.idbodega,
                                                     'idproveedor': producto.idproveedor                                               
                                                   })
        
    return render(request, "appinventario/editarproducto.html", {"miFormulario":miFormulario, "producto_nombreproducto":producto_nombreproducto})        


def busquedaproducto(request):
    return render(request, "appinventario/buscar_producto.html")    

def buscarprod(request):
    if request.GET["nombreproducto"]:
        nombreproducto = request.GET['nombreproducto']
        productos = Producto.objects.filter(nombreproducto__icontains=nombreproducto)
        #envia el ojeto preguntado del get y elfitro realziado a la clase producto y envia ala tabla resulta busqueda productos
        return render(request, "appinventario/res_busqueda_producto.html", {"productos":productos, "nombreproducto":nombreproducto})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos" 

def busquedabodega(request):
    return render(request, "appinventario/buscar_bodega.html")    

def buscarbod(request):
    if request.GET["nombrebodega"]:
        nombrebodega = request.GET['nombrebodega']
        bodegas = Bodega.objects.filter(nombrebodega__icontains=nombrebodega)
        #envia el ojeto preguntado del get y elfitro realziado a la clase producto y envia ala tabla resulta busqueda productos
        return render(request, "appinventario/res_busqueda_bodega.html", {"bodegas":bodegas, "nombrebodega":nombrebodega})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos" 
def busquedaproveedor(request):
    return render(request, "appinventario/buscar_proveedor.html")    

def buscarprove(request):
    if request.GET["empresa"]:
        empresa = request.GET["empresa"]
        proveedores = Proveedor.objects.filter(empresa__icontains=empresa)
        #envia el ojeto preguntado del get y elfitro realziado a la clase producto y envia ala tabla resulta busqueda productos
        #la palabra del a base detaos es la que viaja al formulario de resultad
        return render(request, "appinventario/res_busqueda_proveedor.html", {"proveedores":proveedores, "empresa":empresa})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"         


    #return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})
    
    
    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    
    return HttpResponse(respuesta)
    
class ProductoList(ListView):
   model=Producto
   template_name = "appinventario/producto_list.html"


class ProductoDetalle(DetailView):
    model = Producto
    template_name = "appinventario/producto_detalle.html"
    

class ProductoCreacion(CreateView):
    model=Producto
    success_url = "/appinventario/producto/list"
    fields = ['idproducto','nombreproducto', 'precio','tipo','existencias','idbodega','idproveedor']


class ProductoUpdate(UpdateView):
    model = Producto
    success_url = "/appinventario/producto/list"
    fields = ['idproducto','nombreproducto', 'precio','tipo','existencias','idbodega','idproveedor']
    
class ProductoDelete(DeleteView):
    model = Producto
    success_url = "/appinventario/producto/list"


################
class BodegaList(ListView):
   model=Bodega
   template_name = "appinventario/bodega_list.html"


class BodegaDetalle(DetailView):
    model = Bodega
    template_name = "appinventario/bodega_detalle.html"
    

class BodegaCreacion(CreateView):
    model=Bodega
    success_url = "/appinventario/bodega/list"
    fields = ['idbodega','nombrebodega', 'ubicacion']

class BodegaUpdate(UpdateView):
    model = Bodega
    success_url = "/appinventario/bodega/list"
    fields = ['idbodega','nombrebodega', 'ubicacion']
    
class BodegaDelete(DeleteView):
    model = Bodega
    success_url = "/appinventario/bodega/list"

    ################
class ProveedorList(ListView):
   model=Proveedor
   template_name = "appinventario/proveedor_list.html"


class ProveedorDetalle(DetailView):
    model = Proveedor
    template_name = "appinventario/proveedor_detalle.html"
    

class ProveedorCreacion(CreateView):
    model=Proveedor
    success_url = "/appinventario/proveedor/list"
    fields = ['idproveedor','empresa', 'actividad','email','contacto']

class ProveedorUpdate(UpdateView):
    model = Proveedor
    success_url = "/appinventario/proveedor/list"
    fields = ['idproveedor','empresa', 'actividad','email','contacto']
    
class ProveedorDelete(DeleteView):
    model = Proveedor
    success_url = "/appinventario/proveedor/list"