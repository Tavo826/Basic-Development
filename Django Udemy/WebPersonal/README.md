## Iniciando el proyecto

django-admin startproject WebPersonal

Si se desea cambiar el idioma: settings.py - LANGUAGE_CODE

### Creando la base de datos inicial

settings.py - DATABASE para las configuraciones del motor

*python manage.py makemigrations* para realizar las migraciones de la base de datos

*python manage.py migrate* para aplicar estas migraciones

### Primera App

python manage.py core

Se activa la app en el settings.py del proyecto INSTALLED_APPS

#### views

Se crea una primera vista para la portada llamada home

Se crean las vistas about, portfolio y contact

#### urls

En las urls de la web se importan las views desde la app y se configura la dirección de cada una de las vistas

### plantillas

Se crea dentro de la app una carpeta llamada *templates* en la que se guardan los archivos html

Se crea un primer archivo html llamado *base.html* que contiene la plantilla que se usa como base para las demás. Seguidamente se crean las demás plantillas cada una con su bloque de información

### static

Se crea la carpeta static dentro de la app que contiene una carpeta con el nombre de esta y adentro todos los elementos estáticos necesarios para ver la web en funcionamiento

Estos ficheros se cargan en el template *base-html* en la sección de 'Estilos y fuentes del template

Usando el template tag {% load static %} y en cada link un href="{% static **'ubicación'** %}", tambiém se deben cambiar las imágenes y los scripts al final (si es requerido)