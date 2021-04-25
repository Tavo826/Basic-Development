Se crean las vistas basadas en clases y se llaman en el script *urls.py* con su método **as_view()**.

En la clase de las vistas se crea una función para sobreescribir el diccionario de contexto llamada **get_context_data** y así modificar cualquier clave de este, también se puede sobreescribir el método **get** de la vista para pasar el diccionario de contexto al template como se hacía con las vistas basadas en funciones

#### Vistas CRUD (Create, Read, Update, Delete) con CBV

Se crea un submenú para darle al usuario la opción de crear una página, este menú solo lo verá quien tenga los permisis. Se utiliza el tag **include** para crearlo donde se desea.

Se crea una nueva carpeta dentro de los templates de la app **pages** y allí se crea el template *pages_menu.html* para hacer el menú

Para la creación de páginas se utiliza una vista basada en clases llamada **CreateView**