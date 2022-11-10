from django import forms
from AppCoder.models import Empleados


class buscar_empleado(forms.Form):
      nombre = forms.CharField(max_length=100)


class EmpleadosForm(forms.ModelForm):
  class Meta:
    model = Empleados
    fields = ['nombre', 'apellido', 'direccion', 'numero_documento', 'numero_de_telefono', 'e_mail', 'contrasena']