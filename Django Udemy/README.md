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