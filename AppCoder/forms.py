from django import forms
from AppCoder.models import Pedidos


class buscar_empleado(forms.Form):
  nombre = forms.CharField(max_length=100)


class PedidosForm(forms.ModelForm):
  class Meta:
    model = Pedidos
    fields = ['nombre_cliente', 'empleado', 'pedido', 'estado', 'fecha'] #-> saque la fecha por que la voy a poner automatico


"""
class ProductosForm(forms.ModelForm):
  class Meta:
    model = Productos
    fields = ['nombre_producto', 'ingredientes', 'descripcion', 'codigo_producto']

"""