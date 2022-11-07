# Proyecto Final Grupal correspondiente a Python dictado por Coderhouse

Comision: 44065 Profesor: German Martinez Tutor: Esteban Acevedo

Grupo Conformado por:

    Carolina Cartategui
    Claudio Ruhlmann
    Christian Porcel de Peralta

El ejemplo de MVT contiene codigo de:

    Modelos
    Vistas
    Templates

Chequear que este instalado Python

Para comenzar primero tienen que asegurarse que tienen instalado, python.

En windows tiene que abrir una terminal cmd o powershell.

PS C:\> python --version
Python 3.X.X 

En Linux/Mac tiene que abrir una terminal bash

$ python --version
Python 3.X.X 

Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este link.
Instalar django

En una terminal cmd o powershell desde windows:

C:\> pip install django

Linux/Mac:

$ pip install django

Si no arrojo errores esto es suficiente para poder correr el projecto.
Clonar el projecto con git

Windows:

C:\> git clone https://github.com/Carocartategui/mi-primer-mvt

Linux/Mac:

$ git clone https://github.com/Carocartategui/mi-primer-mvt

Correr el Servidor

Los siguientes comandos son analogos en Mac/Linux/Windows:

cd mi-primer-mvt
python manage.py migrate

La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

python manage.py runserver

Listo ya tienes corriendo el servidor web.

Ahora has click en el siguiente link para ver el ejemplo corriendo:

http://localhost:8000/