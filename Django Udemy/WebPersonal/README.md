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

#### plantillas

Se crea dentro de la app una carpeta llamada *templates* en la que se guardan los archivos html

Se crea un primer archivo html llamado *base.html* que contiene la plantilla que se usa como base para las demás. Seguidamente se crean las demás plantillas cada una con su bloque de información

#### static

Se crea la carpeta static dentro de la app que contiene una carpeta con el nombre de esta y adentro todos los elementos estáticos necesarios para ver la web en funcionamiento

Estos ficheros se cargan en el template *base-html* en la sección de 'Estilos y fuentes del template

Usando el template tag {% load static %} y en cada link un href="{% static **'ubicación'** %}", tambiém se deben cambiar las imágenes y los scripts al final (si es requerido)

### Segunda app

Se crea una app nueva llamada *porfolio* para gestionar los proyectos de la web, estos se guardarán en una base de datos con su título, descripción, enlace e imagen

#### Modelos

Se crea una clase *Project* que contendrá los datos de los proyectos y se registra en el fichero *admin.py* de la app

#### Modificando Admin (1)

Se modifica la forma en que se muestra el nombre de la app portfolio agregando en el script *apps.py* la línea:

verbose_name = 'Portafolio'

Para validar este cambio, se modifica en el *settings.py* las apps instaladas teniendo en cuenta el nombre de la clase en *apps.py*

'portfolio' -> 'portfolio.apps.PortfolioConfig'

Se modifica el nombre en que se muestra el modelo Project agregando una metaclase con los siguientes atributos

*verbose_name = 'proyecto'* para el nombre en singular
*verbose_name_plural = 'proyectos'* para el nombre en plural
*ordering = ['-created']* para ordenar las entradas por fecha de creación (de más nuevo a más antiguo *guion*)

Se modifica la forma como se visualizan las publicaciones, creando la función *__str__* y retornando el título del proyecto, también se posibilita la visualización de la fecha de creación y de edición creando en el script *admin.py* una clase **ProjectAdmin** en la cual se definen como campos de lectura

readonly_fields = ('created', updated')

Finalmente se añade como configuración extendida al registro del modelo en este mismo script

admin.site.register(Project) -> admin.site.register(Project, ProjectAdmin)

La configuración para poder visualizar las imágenes de las publicaciones se realizan el el script *settings.py* añadiendo al final las direcciones de la carpeta que se crea para guardar dichas imágenes

*MEDIA_URL = '/media/'* dirección pública
*MEDIA_ROOT = os.path.join(BASE_DIR, 'media')* dirección privada

Finalmente estas dos variables se importan en el script *urls.py* del proyecto para que el sistema sepa dónde tiene que ir a buscar la imagen

#### Modelo-Vista-Template

Para recuperar los datos del portfolio dentro de la misma app, se lleva del archivo *views.py* del proyecto original (core) al archivo *views.py* de la app, lo mismo se hace con el template html, finalmente se modifica el script *urls.py* para que busque la vista en la app

#### Lista de publicaciones

Para recuperar esta lista en la view

Project.objects.all()