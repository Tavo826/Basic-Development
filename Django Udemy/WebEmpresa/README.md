**Páginas estáticas:** Portada, Historia, Visítanos - Se manejan en la app core
**Páginas dinámicas:** Servicios, Blog - Se manejan en sus respectivas apps

En el pie de página se encuentran enlaces a redes sociales y páginas genéricas. Las redes sociales se gestionan en una app *social*, las páginas genéricas se gestionan en la app *pages*

La sección de contacto se gestiona en su propia app

### Mejorando el manejo de las urls

Se crean configuraciones urls específicas para cada app y luego se importan en el fichero *urls.py* del proyecto bajo una url global

### Resaltando la sección actual

Se espera que en el menú se resalte la sección en la que se encuentra actualmente, esto se hace utilizando la clase 'active' en el script *base.html*