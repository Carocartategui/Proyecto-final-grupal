"""
from AppCoder.models import Empleados

Empleados(nombre="Rosario", apellido="Gomez", direccion="Rio Parana 745", numero_documento=123123, numero_de_telefono=1165588978, e_mail="rosariogomez@gmail.com", contrasena="123456").save()
Empleados(nombre="Juan", apellido="Perez", direccion="Av Centenario 1745", numero_documento=35621478, numero_de_telefono=1158963258, e_mail="juanperez@gmail.com", contrasena="123456").save()
Empleados(nombre="Martin", apellido="Bolazo", direccion="Av Belgrano 1234", numero_documento=12852369, numero_de_telefono=1125631478, e_mail="martinbolazo@gmail.com", contrasena="123456").save()
Empleados(nombre="Monica", apellido="Gutierrez", direccion="Vuelta de Obligado 1478", numero_documento=35789452, numero_de_telefono=1141789562, e_mail="monicagutierrez@gmail.com", contrasena="123456").save()

print("Se cargo con éxito los usuarios de pruebas")
"""
from AppCoder.models import Pedidos

Pedidos(nombre_cliente="Rosario", empleado="Gomez", pedido="muza", estado="entregado", fecha="17/04/2018").save()

print("Se cargo con éxito los pedidos de pruebas")