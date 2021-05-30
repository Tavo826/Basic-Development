#Script que hace las tareas del carrito

class Carro:
    #Detectando la petición para acceder al carro
    def __init__(self, request):
        self.request = request
        #Construyendo la sesión
        self.session = request.session
        #Iniciar carro
        carro = self.session.get('carro')

        #Si no tiene carro inicializado
        if not carro:
            #Se crea el carro
            carro = self.session['carro'] = {}

        #Si se va a otra página y vuelve, se muestra el carro que tenía
        #else:
        #Recupera el carro
        self.carro = carro

    def agregar(self, producto):
        #Se agrega el producto si no está en el carro
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url
            }
        
        #Si el producto ya está en el carro, se incrementa una unidad
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] += 1
                    break
        
        #Se actualiza el carro para almacenarlo en la sesión
        self.guardar_carro()

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    #Eliminar un producto
    def eliminar(self, producto):
        producto.id = str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    #Restar unidades de un producto
    def restar_producto(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] -= 1
                    if value['cantidad'] < 1:
                        self.eliminar(producto)
                    break

        self.guardar_carro()

    #Vaciar el carro
    def limpiar_carro(self):
        self.session['carro'] = ''
        self.session.modified = True