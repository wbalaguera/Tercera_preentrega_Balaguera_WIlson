from django import forms


class ProductoFormulario(forms.Form):
    #Especificar los campos
    idproducto=forms.IntegerField()
    nombreproducto=forms.CharField()
    tipo=forms.CharField()
    precio=forms.IntegerField()
    existencias=forms.IntegerField()
    idbodega=forms.IntegerField()
    idproveedor=forms.IntegerField()

  
class ProveedorFormulario(forms.Form):
    idproveedor=forms.IntegerField()
    empresa=forms.CharField()
    actividad=forms.CharField()
    email = forms.EmailField()
    contacto=forms.CharField()

class BodegaFormulario(forms.Form):
    idbodega=forms.IntegerField()
    nombrebodega=forms.CharField()
    ubicacion=forms.CharField()
        