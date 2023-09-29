class Mensaje:
    def __init__(self):
        self.Producto = None
        self.cantidad_solicitud: 0

    def imprimir(self):
        print(f"Se solicta {self.cantidad} del siguiente producto {self.Producto.nombre} ")
    
    