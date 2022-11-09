from django import forms
from AppCoder.models import Empleados

from django import forms
  class BuscarEmpleado(forms.Form):
      nombre = forms.CharField(max_length=100)


class EmpleadosForm(forms.ModelForm):
  class Meta:
    model = Empleados
    fields = ['nombre', 'apellido', 'direccion', 'numero_documento,'numero_de_telefono', 'E_mail', 'contrasena']