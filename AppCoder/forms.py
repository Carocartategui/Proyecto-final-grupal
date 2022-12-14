from django import forms
from AppCoder.models import Pedidos, Empleados


class buscar_empleado(forms.Form):
  nombre = forms.CharField(max_length=100)


class PedidosForm(forms.ModelForm):
  class Meta:
    model = Pedidos
    fields = ['nombre_cliente', 'empleado', 'pedido', 'estado', 'fecha'] #-> saque la fecha por que la voy a poner automatico

class EmpleadosForm(forms.ModelForm):
  class Meta:
    model = Empleados
    fields = ['nombre', 'apellido', 'direccion', 'numero_documento', 'numero_de_telefono', 'e_mail', 'contrasena']

