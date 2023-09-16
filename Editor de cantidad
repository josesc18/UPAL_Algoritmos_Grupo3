def modificar_cantidad(nombre_producto, nueva_cantidad, lista_enlazada):
    nodo_actual = lista_enlazada.lista
    while nodo_actual is not None:
        if nodo_actual.valor.nombre == nombre_producto:
            try:
                nueva_cantidad = int(nueva_cantidad)
                nodo_actual.valor.cantidad = nueva_cantidad
                print(f"Se ha modificado la cantidad del producto '{nombre_producto}' a {nueva_cantidad}")
                return
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
                return

        nodo_actual = nodo_actual.puntero
    print(f"No se encontró un producto con el nombre '{nombre_producto}'")
