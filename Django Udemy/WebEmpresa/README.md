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

