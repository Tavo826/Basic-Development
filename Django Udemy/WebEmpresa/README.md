**Páginas estáticas:** Portada, Historia, Visítanos - Se manejan en la app core

**Páginas dinámicas:** Servicios, Blog - Se manejan en sus respectivas apps

En el pie de página se encuentran enlaces a redes sociales y páginas genéricas. Las redes sociales se gestionan en una app *social*, las páginas genéricas se gestionan en la app *pages*

La sección de contacto se gestiona en su propia app

### Mejorando el manejo de las urls

Se crean configuraciones urls específicas para cada app y luego se importan en el fichero *urls.py* del proyecto bajo una url global

### Resaltando la sección actual

Se espera que en el menú se resalte la sección en la que se encuentra actualmente, esto se hace utilizando la clase 'active' en el script *base.html*

### Relaciones entre modelos en la app **blog**

Se crea en el script *models.py* la clase **Category** con el nombre de la categoría y los campos de creación y edición. Y la clase **Post** que contiene título, conenido, fecha de publicación(manual), imagen, autor, categorías y los campos de creación y edición.

Para realizar la relación del autor, se importa el usuario del modelo *users*, posterior a esto se crea un campo de clave foránea y se pasa como parámetro el usuario

author = models.ForeingKey(User, verbose_name='Autor', on_delete=models.CASCADE)

Para las categorías, se pretende agregar varias a una misma entrada, se crea un campo de muchos a muchos y se pasa la clase categoría como parámetro

categories = models.ManyToManyField(Category, verbose_name='Categorías')

### Procesadores de contexto

Con esto se pretende recuperar los link de las redes sociales que se añadan en la app social

#### Prueba

Se crea dentro de la app **social** un script llamado *processors.py* y allí se crea una función **context_dict** que retorna un diccionario. En el script *settings.py* se modifica dentro de la variable **TEMPLATES**, la clave **context_processors** añadiendo la función

'social.processors.context_dict'


### Template tags propios

Se encarga de recuperar y devolver la lista de páginas secundarias

Se crea dentro de la app **pages** el directorio **templatetags** y dentro de este se crean los scripts *__init__.py* y *pages_extras.py*. Dentro de este se registra en templates **from django import template** y se importa el modelo **from pages.models import Page**. Se crea una función para recuperar la lista de páginas

def get_page_list():
    pages = Page.objects.all()
    return pages

Se registra el template tag

register = template.Lybrary()

Y se añade un decorador a la función 

@register.simple_tag

En el template *base.html* se modifican los enlaces de las páginas externas, se carga el script *pages_extras.py* y se llama la función del template tag como una variable y se recorre con un for para mostrarlas

### Orden manual de las páginas secundarias

En el modelo *Page* se agrega un campo de tipo **SmalIntegerField** y se cambia la prioridad del orden en la subclase *Meta*

ordering = ['title'] -> ordering = ['order','title']

Finalmente se agrega en el admin

list_display = ['title', 'order']

#### Edición directa

Destecta el tipo de usuario y habilita un botón en el front que lo lleva a la edición de la página. Se accede al usuario activo en el template *sample.html* **{{user}}**, este boton debe apuntar a la edición de cada página secundaria del admin **admin:pages_page_change**

### Añadiendo un editor de texto

Se añade el editor **ckeditor** a las apps instaladas del *settings.py*. En el script *models.py* se importa 

from ckeditor.fields import RichTextField

Y para usarlo se modifica el campo **content** del modelo sustituyendo **models.TextField** por **RichTextField**

Para establecer una configuración personaliada de la barra de herramientas, se crea el diccionario **CKEDITOR_CONFIGS** y se cambian sus valores por defecto

Para que django interprete los cambios que se realizan en el texto, en el template *sample.html*

{{page.content|linebreacks}} -> {{page.content|safe}}

### Formulario de contacto

Se crea *forms.py* dentro de la app **contact**, se importa la librería forms y se crea una clase con los campos de nombre, correo y contenido, al enviar el formulario se debe tener en cuenta la verificación CSRF, generando el token en el formulario

{% csrf_token %}

#### Enviar el correo

Se importa la librería **EmailMessage** y se modifica la vista con los datos y la forma en que se recibe el correo

### Personalizar el ADMIN (4)

Modificando los permisos de acceso, en el admin se crea un grupo **Personal** para los clientes con permisos completos para el blog, las páginas y los servicios, para la app social tiene permiso de ver y cambiar el enlace. Al crear el usuario se debe señalar la opción **Es staff** y se le asigna al grupo **Personal**.

Se modifica el script *admin.py* de la app **social** para que el nombre clave y el de la red solo sean de lectura para el personal