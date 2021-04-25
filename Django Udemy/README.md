## DJANGO

Promueve la filosofía del desarrollo ágil y extensible, aplicando el pricipio DRY (Don't Repeat Yourself)

### Características importantes:

* Cuenta con un sistema basado en componentes reutilizables (apps).
* Tiene un mapeador ORM para manejar registros de la BD como objetos.
* Panel de administrador para gestionar objetos a través de formularios.
* Sistema de plantillas extensibles con herencia basado en etiquetas.

### Iniciar un proyecto

django-admin startproject **NombreProyecto**

### Apps

Forma en que se organiza el código para ser reutilizado, sirven para gestionar el panel de administrador, la autenticación de los usuarios, entre otros.

Las apps activas se encuentran en settings.py - INSTALLED_APPS

python manage.py startapp **NombreApp** para crear una app

### Vistas

Hacen referencia a la lógica que se ejecuta cuando se hace una petición a la Web

### Urls

Administran la dirección en la que se va a mostrar cada una de las vistas

### Ficheros estáticos (configuración)

Django no puede trabajar con los ficheros estáticos predefinidos en el frontend, para ver cómo quedaría la página finalizada se deben realizar algunas configuraciones

Se crea una carpeta static dentro de la app y se copia allí los recursos estáticos necesarios para la app

### Modelos

Son las clases que están enlazadas a la base de datos de la app, cada clase representa una tabla en la base de datos

### Crear superusuario ADMIN

Es necesario para ingresar el administrador de Django en el que se pueden modificar los modelos del proyecto, los cuales deben estar registrados previamente en el fichero **admin.py** de la app

python manage.py createsuperuser

#### Personalizar el ADMIN (1)

Para modificar el nombre de la app se agrega en el script *apps.py* de la app, la variable **verbose_name** con el nombre que se desea que aparezca, para validar esta acción se debe modificar en la lista **INSTALED_APPS** del script *settings.py* del proyecto:

'portfolio.apps.NombreClase'

Para modificar el nombre del modelo se crea una subclase dentro de la misma clase llamada **Meta** para añadir metadatos extendidos en la que se puede agregar el nombre con que se desea ver el modelo tanto en singular (verbose_name) como en plural (verbose_name_plural), también se puede agregar un campo para ordenar los registros utilizando la variable 

ordering = [lista de atributos con los que se desea ordenar]

Para modificar la foma como se ven las publicaciones en el ADMIN se agrega dentro de la subclase una función *__str__(self)* y retornando de esta el parámetro qeu se desee

Para que se pueda visualizar la fecha de cración y de edición de cada publicación, en el script *admin.py* se crea una clase para extender las funcionalidades del ADMIN, en ella se redefinen el 'created' y el 'updated' como campos de lectura

Para mostrar las imágenes de las publicaciones, como primera medida se guardan en la raíz del proyecto en una carpeta llamada *media*, esta carpeta se registra en el fichero *settings.py*, añadiendo al final la dirección pública de la carpeta (MEDIA_URL), la dirección privada de la carpeta (MEDIA_ROOT). Luego de esto, siempre que se tenga el bug en True, se debe añadir una configuración extendida. En el fichero *urls.py* del proyecto.

### Patrón MVT: Modelo-Vista-Template

Cuando se trabaja con bases de datos y modelos, el proceso que sigue Django es el siguiente:

* Se recibe la petición
* Se pasa a la vista
* En la vista se recuperan los datos del modelo correspondiente
* Se renderiza el template, integrando los datos dinámicos del modelos que se pasa desde la vista, antes de que el navegador muestre el html resultante

### Relaciones entre modelos

#### Relaciones con foreign keys:

Permiten enlazar una insancia de un modelo con otra instancia de otro modelo, o del mismo. Un ejemplo es el enlace de una entrada con un usuario que representa al autor

#### Relaciones many to many: 

Permiten enlazar varias instancias. Un ejemplo es la asignación de varias categorías a una sola entrada.

#### Personalizar el ADMIN (2)

En el script *admin.py* de la app se puede modificar las columnas que se desean mostrar en el admin

list_display = (*args,)

También se pueden ordenar las entradas por uno o varios campos

ordering = (*args,)

Se puede mostrar un formulario de búsqueda

search_fields = (args*,)

Para poder buscar por autor, al hacer parte de un modelo relacional foreign key

search_fields = ('author__username',)

Para poder buscar por categorías, al hacer parte de un modelo relacional many to many

search_fields = ('categories__name',)

Se puede usar una gerarquía de fechas para modelos con campos DateTime

date_hierarchy = *arg

Finalmente se puede crear una lista de campos con los que se desea filtrar, normalmente son relaciones

list_filter = (*args,)

Para mostrar los elementos relacionados en campos many to many se crea un método dentro de la clase

### Procesadores de contexto

Se utilizan para recuperar los enlaces de las páginas web, se entiende como contexto un diccionario común que contiene información que puede extenderse a todos los templates y así no enviar esta información desde la vista

Si se tiene creado un diccionario y se desea que este extienda el proceso global, en el script *settings.py* la variable **TEMPLATES** contiene una clave llamada *OPTIONS* y dentro de los procesadores de contexto se añade dicho diccionario

### Template tags propios

Muestra un contenido personalizado. Es una herramienta más flexible al procesador de contexto, pero consume más recursos porque se debe ejecutar el template tag en cada template, en comparación co el procesdor de contexto que ya está inyectado en todos los templates

#### Creación del template tag

Se crea dentro de la app un directorio llamado **templatetags**, dentro de este se indica que es un package creando el script *__init__.py*. Segidamente se crea un segundo fichero y se registra dentro de la librería de templates escribiendo **from django import template**, y también se importa el modelo que se va a utilizar. Se crea un función para recuperar el contenido y lo devuelva al template en forma de template tag, este template tag debe registrarse en la librería de templates, se crea una variable donde se hace referencia a la librería **template.Library()** y se añade un decorador a la función del template tag **@'variable'.simple_tag**. Finalmente se modifica el template donde se quiera usar

### Orden manual de los modelos

Orden manual de las páginas secundarias, en el modelo que se quiere ordenar, se agrega un nuevo campo de tipo **SmallIntegerField**, luego se cambia la variable **ordering** dándole prioridad al campo que se acaba de crear. Luego de esto se agrega una variable en el admin que permita visualizar los campos de ordenamiento

### Edición directa de un modelo

Destecta el tipo de usuario y habilita un botón en el front que lo lleva a la edición de la página. Para conocer el tipo de usuario, este se guarda en el contexto ubicado en el script *settings.py* **django.contrib.auth.context_processors.auth** lo que permite que se pueda visualizar desde cualquier template

### Personalizar el ADMIN (3)

Añadir un editor de texto wysiwyg (what you see is what you get), en este caso el *ckeditor*, para esto se debe tener instalada la librería **django-ckeditor**, luego se añade a las apps instaladas en *settings.py* y se modifica el modelo donde se quiera agregar

Para establecer una configuración personalizada básica se debe redefinir su diccionario de configuración en *settings.py*. Se crea un diccionario **CKEDITOR_CONFIGS** y dentro de la clade **defautlt** se pueden cambiar parámetros como

* 'toolbar': None -> muestra todas las opciones de la barra de herramientas
* 'toolbar': 'Basic' -> muestra un diseño simple con negritas y cursivas

Para que django interprete los cambios que se realizan en el texto, se cambia el template donde se use la variable de contenido del modelo

### Formularios

Se crean en un script *forms.py* dentro de la app, allí se importa la librería **forms** y se declara una clase con los campos necesarios para el modelo

#### Enviar formulario por correo

Para hacer pruebas se puede hacer con **Mailtrap.io** y copiar la configuración en *settings.py*

### Personalizar el ADMIN (4)

Modificando los permisos de los usuarios, se crea un grupo en el admin y se les da los permisos, cada modelo tiene 4 permisos añadir, cambiar, borrar y ver. También puede ser necesario que algunos campos sean de solo lectura, esto se hace en el script *admin.py* de la app

### Vistas basadas en clases

**FBV** (vistas basadas en funciones)

**CBV** (vistas basadas en clases)

Las CBV:

* Sirven como moldes

* Contienen atributos y métodos

* Permiten el uso de herencia

Los tipos de vistas blasadas en clases se dividen en grupos 

* **autenticación:** LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

* **genéricas de detalles:** DetailView
 
* **genéricas de edición:** CreatedView, DeleteView, FormView, UpdateView

* **genéricas de base:** RedirectView, TemplateView, View

* **genéricas de listas:** ListView

* **genéricas de fechas:** ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, TodayArchiveView, WeekArchiveView, YearArchiveView

Estas vistas se deben llamar de manera diferente en el script *urls.py*. Dentro de la clase creada en las vistas, se puede sobreescribir el diccionario de contexto por si se desea enviar información

#### Vistas CRUD (Create, Read, Update, Delete) con CBV

Se le da al ususario la opción de administrar las páginas a través de un menú que solamente les aparece a ellos.