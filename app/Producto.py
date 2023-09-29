class Producto:
    def __init__(self):
        self.nombre = ""
        self.cantidad = 0

    def sin_stock(self):
        print(f"Producto {self.nombre} sin stock")

    def imprimir(self):
        print(f"Producto {self.nombre} Cantidad en Stock {self.cantidad}")