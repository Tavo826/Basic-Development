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

### Pruebas unitarias

Se pretende crear un usuario para luego comprobar que se creó un perfil para este en el script *test.py* de la app **registration**

Se ejecuta el test

python manage.py test registration

### Paginación

Se modifica en las vistas de la app **profiles** y se organiza en el templaet *profile_list.html*

### Principio de las 5 W

* **Who:** Un usuario registrado e identificado

* **What:** Establecer un chat privado entre el susuario y otros usuarios para que se puedan comunicar

* **When:** Cuando un usuario decida iniciar una conversación con otro

* **Where:** En su debida sección de Mensajes o a través del botón "Enviar mensaje" en los perfiles públicos

* **Why:** Porque ofrecer una vía de comunicación privada es una opción que toda aplicación social debería incluir

El sistema de mensajes (app messenger) no será en tiempo real, sino un sistema más simple parecido a un email interno que el usuario deberá comprobar manualmente

### TTD (Test Driven Development o Desarrollo Guiado por Pruebas)

Ya teniendo los modelos creados en la app **messenger** se pueden realizar algunas pruebas antes de realizar las vistas, para saber si funcionan correctamente

En el fichero *test.py* se crean algunos test para probar los modelos

#### Model Manager

Se pretende que sea más fácil recuperar un hilo a través de sus usuarios, sin tener que aplicar el filtro 2 veces, para esto se crea una consulta propia **find** en el modelo para recuperar una instancia a partir de los usuarios de entrada. Para crear el administrador, se crea una clase llamada **ThreadMnager

## Peticiones asíncronas

Se hace innecesario crear un formulario para cargar los mensajes de la app messenger. Es la manera idea de enviar mensajes sin recargar toda la página