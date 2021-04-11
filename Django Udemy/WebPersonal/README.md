## Iniciando el proyecto

django-admin startproject WebPersonal

Si se desea cambiar el idioma: settings.py - LANGUAGE_CODE

### Creando la base de datos inicial

settings.py - DATABASE para las configuraciones del motor

*python manage.py makemigrations* para realizar las migraciones de la base de datos

*python manage.py migrate* para aplicar estas migraciones

### Primera App

python manage.py core

#### views

Se crea una primera vista para la portada llamada home

Se crea la vista about

#### urls

En las urls de la web se importan las views desde la app y se configura la dirección de cada una de las vistas