from app.Database import ListaEnlazada
from app.Producto import Producto

# Crea instancias de las clases
lista = ListaEnlazada()
producto = Producto()

# Configura las propiedades del objeto Producto
producto.cantidad = 50
producto.cantidad_minima = 5
producto.correo_provedor = "jose.sanchez.alu@upal.edu.pe"
producto.nombre = "Ejemplo"
producto.stock_pedido = 4

producto2 = Producto()

# Configura las propiedades del objeto Producto
producto2.cantidad = 50
producto2.cantidad_minima = 5
producto2.correo_provedor = "jose.sanchez.alu@upal.edu.pe"
producto2.nombre = "Ejemplo 2"
producto2.stock_pedido = 4


producto3 = Producto()

# Configura las propiedades del objeto Producto
producto3.cantidad = 50
producto3.cantidad_minima = 5
producto3.correo_provedor = "jose.sanchez.alu@upal.edu.pe"
producto3.nombre = "Ejemplo 3"
producto3.stock_pedido = 4
# Inserta el producto en la lista enlazada
lista.insertarAlFinal(producto)
lista.insertarAlFinal(producto2)
lista.insertarAlFinal(producto3)
lista.imprimirNodos()

lista.eliminarSegunValor("Ejemplo 2")

lista.imprimirNodos()

