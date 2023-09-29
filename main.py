from app.Database import ListaEnlazada
from app.Producto import Producto
from app.Notificaciones import Notificaciones
from app.Mensaje import Mensaje
# Crea instancias de las clases
lista = ListaEnlazada()
notificaciones = Notificaciones()

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Registrar Producto', accion1),
        '2': ('Listar Productos', accion4),
        '3': ('Vender Producto', accion2),
        '4': ('Ver productos sin Stock', accion5),
        '5': ('Solicitar Stock', accion3),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


def accion1():
    producto = Producto()
    producto.nombre = input("Ingrese una nombre del producto: ")
    producto.cantidad = int(input("Ingrese una cantidad del producto: "))
    lista.insertarAlFinal(producto)
    print('Producto Registrado')
    lista.imprimirNodos()

def accion2():
    nombre = input("Ingrese una nombre del producto: ")
    cantidad = int(input("Ingrese cantidad a vender: "))
    producto = lista.buscar_por_nombre(nombre)
    producto_cantidad = producto.valor.cantidad

    if(producto_cantidad >= cantidad):
        nueva_cantidad = producto_cantidad - cantidad
        lista.modificar_cantidad(nombre, nueva_cantidad)
        producto = lista.buscar_por_nombre(nombre)
        if(nueva_cantidad == 0 ):
            agregar_producto = Producto()
            agregar_producto.nombre = producto.valor.nombre
            agregar_producto.cantidad = producto.valor.cantidad
            queue = Mensaje()
            queue.Producto = agregar_producto
            queue.cantidad_solicitud = 20
            notificaciones.enqueue(queue)
               
        print(f"El prodcuto {producto.valor.nombre} cuenta con un total de {producto.valor.cantidad} en stock")
    else:
        print("No tiene el stock suficiente para vender el producto")


def accion3():
    notificaciones.enviar_notificaciones()

def accion4():
    lista.imprimirNodos()

def accion5():
    notificaciones.sin_stcok()

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()

