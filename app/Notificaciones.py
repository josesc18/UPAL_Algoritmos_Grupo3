from app.Database import Nodo

class Notificaciones:
    def __init__(self):
        self.longitud = 0
        self.head = None
        self.tail = None

    def enqueue(self, valor):
        nodo = Nodo(valor)
        if self.longitud == 0:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.puntero = nodo
            self.tail = nodo
        self.longitud += 1
           

    def dequeue(self):
        if self.longitud > 0:
            self.head = self.head.puntero
            self.longitud -= 1
        
    def enviar_notificaciones(self):
        nodo_actual = self.head
        while nodo_actual is not None:
            cantidad_solicitud = nodo_actual.valor.cantidad_solicitud
            nombre_producto = nodo_actual.valor.Producto.nombre
            print(f"Se solicita al proveedor un stock de {cantidad_solicitud} del producto: {nombre_producto}")
            self.dequeue()
            nodo_actual = nodo_actual.puntero
            

