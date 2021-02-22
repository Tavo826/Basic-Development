**API != Servicios web != api rest != api soap**

Una **API** (Application Programming Interface) se refiere a un conjunto de métodos previamente definidos que se requieren implementar por un usuario, permitiendo separar la implementación de los métodos (por ejemplo crear o modificar una carpeta en el computador sin tener que modificar directamente el código del sistema operativo)

Una **API Web** es la comunicación mediante el protocolo http entre 2 sistemas, este protocolo cliente-servidor permite la comunicación mediante mensajes.

Mensaje cliente -> servidor: **Request**

Mensaje servidor -> cliente: **Response**

Los servicios web contienen dos arquitecturas dominantes: 
* *Api Soap(Simple Object Access Protocol):* protocolo oficial de WWW
* *Api Rest(Representation State Transfer):* conjunto de principios arquitectónicos. 

Para que un servicio sea rest se deben cumplir 6 pricipios:

**1** Desacoplamiento entre el cliente y el servidor

**2** Comunicación entre cliente y servidor sin estado (no se almacena info de las solicitudes). EN la request va toda la información necesaria

**3** Interface uniforme, recursos identificados mediante una url

**4** Se guarda en caché las peticiones anteriores

**5** Sistema en capas organizado en jerarquías invisibles para el cliente

**6** Código disponible según se necesite