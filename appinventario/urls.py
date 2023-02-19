from django.urls import path
from appinventario import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from AppCoder import curso
#views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('productos', views.productos, name="Productos"),
    path('leerproducto', views.leerproducto, name="LeerProductos"),
    path('eliminarproducto/<producto_nombreproducto>/', views.eliminarproducto, name="EliminarProductos"),
    path('editarproducto/<producto_nombreproducto>/', views.editarproducto, name="EditarProductos"),
    path('buscarprod/', views.buscarprod),
    path('buscar_producto', views.busquedaproducto, name="BuscarProductos"),

    path('proveedores', views.proveedores, name="Proveedores"),
    path('leerproveedor', views.leerproveedor, name="LeerProveedores"),
    path('eliminarproveedor/<proveedor_empresa>/', views.eliminarproveedor, name="EliminarProveedores"),
    path('editarproveedor/<proveedor_empresa>/', views.editarproveedor, name="EditarProveedores"),
    path('buscarprove/', views.buscarprove),
    path('buscar_proveedor', views.busquedaproveedor, name="BuscarProveedores"),
    
    path('bodegas', views.bodegas, name="Bodegas"),
    path('leerbodega', views.leerbodega, name="LeerBodegas"),
    path('eliminarbodega/<bodega_nombrebodega>/', views.eliminarbodega, name="EliminarBodegas"),
    path('editarbodega/<bodega_nombrebodega>/', views.editarbodega, name="EditarBodegas"),
    path('buscarbod/', views.buscarbod),
    path('buscar_bodega', views.busquedabodega, name="BuscarBodegas"),



    path('producto/list', views.ProductoList.as_view(), name='ListProducto'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='DetailProducto'),
 
    path(r'^nuevoprod$', views.ProductoCreacion.as_view(), name='NewProducto'),
    path(r'^editarprod/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='EditProducto'),
    path(r'^borrarprod/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='DeleteProducto'),


    path('bodega/list', views.BodegaList.as_view(), name='ListBodega'),
    path(r'^detailbodega(?P<pk>\d+)$', views.BodegaDetalle.as_view(), name='DetailBodega'),
    path(r'^nuevobod$', views.BodegaCreacion.as_view(), name='NewBodega'),
    path(r'^editarbod/(?P<pk>\d+)$', views.BodegaUpdate.as_view(), name='EditBodega'),
    path(r'^borrarbod/(?P<pk>\d+)$', views.BodegaDelete.as_view(), name='DeleteBodega'),

    path('proveedor/list', views.ProveedorList.as_view(), name='ListProveedor'),
    path(r'^detailprov(?P<pk>\d+)$', views.ProveedorDetalle.as_view(), name='DetailProveedor'),
    path(r'^nuevoprov$', views.ProveedorCreacion.as_view(), name='NewProveedor'),
    path(r'^editarprov/(?P<pk>\d+)$', views.ProveedorUpdate.as_view(), name='EditProveedor'),
    path(r'^borrarprov/(?P<pk>\d+)$', views.ProveedorDelete.as_view(), name='DeleteProveedor'),
      
]

urlpatterns += staticfiles_urlpatterns()