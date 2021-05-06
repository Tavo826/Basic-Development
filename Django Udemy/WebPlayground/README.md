Se crean las vistas basadas en clases y se llaman en el script *urls.py* con su método **as_view()**.

En la clase de las vistas se crea una función para sobreescribir el diccionario de contexto llamada **get_context_data** y así modificar cualquier clave de este, también se puede sobreescribir el método **get** de la vista para pasar el diccionario de contexto al template como se hacía con las vistas basadas en funciones

#### Vistas CRUD (Create, Read, Update, Delete) con CBV

Se crea un submenú para darle al usuario la opción de crear una página, este menú solo lo verá quien tenga los permisis. Se utiliza el tag **include** para crearlo donde se desea.

Se crea una nueva carpeta dentro de los templates de la app **pages** y allí se crea el template *pages_menu.html* para hacer el menú

Se crean las vistas para crear, editar o eliminar una página, cada una con sus respectivos parámetros

#### Personalizar el formulario de las CBV

Se crea en *forms.py* y como está enlazado a un modelo, se puede generar automáticamente, sin necesidad de cearlo desde cero, para esto se crea una subclase **Meta** y se enlaza el modelo, por último se cambian las vistas con este formulario

Se modifica el tamaño del contenido de las páginas en un css y inyectan en el administrador y en el formulario

### Mixin de identificación

Se crea la clase **StaffRequiredMixin** con la intención de que la vista que la herede tenga como condición que el usuario tenga los permisos para entrar

### Decoradores de identificación

Se modifica la clase **StaffRequiredMixin** agregando el decorador **staff_member_required** y así ahorrarse la comprobación del usuario dentro de la clase y como plus lo redirige a la página a la que quería entrar en un principio.

Un mejor uso es aplicar el decorador directamente a las vistas basadas en clases, y así no tener que crear el mixin

### Configurar un servidor SMTP para pruebas

Simula que envía los correos pero en realidad los guarda en forma de ficheros dentro de un directorio del proyecto. Esta configuración se realiza en el 'settings.py' del proyecto

### Señales

En el proyecto se pretende que después de que se un usuario se registre, se cree un perfil de este.

