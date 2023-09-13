class Nodo:
    def __init__(self, valor ):
        self.valor = valor
        self.puntero = None

class ListaEnlazada:
    def __init__(self):
        self.longitud = 0
        self.lista= None

    def insertarAlFinal(self, valor):
        mi_nodo = Nodo(valor)
        if self.longitud == 0:
            self.lista = mi_nodo
        else:
            nodo_actual = self.lista
            while nodo_actual.puntero != None:
                nodo_actual = nodo_actual.puntero
            nodo_actual.puntero = mi_nodo
        self.longitud += 1

    def eliminarSegunValor(self, valor):
        if self.longitud == 0:
            return False
        else:
            nodo_actual = self.lista
            try:
                if nodo_actual.valor.nombre == valor:
                    self.lista = nodo_actual.puntero
                    nodo_actual.puntero = None
                else:
                    while nodo_actual.puntero.valor.nombre != valor:
                        nodo_actual = nodo_actual.puntero
                    borrar = nodo_actual.puntero
                    nodo_actual.puntero = borrar.puntero
            except AttributeError:
                return False
        self.longitud = self.longitud - 1

    def imprimirNodos(self):
        nodo_actual = self.lista
        while nodo_actual is not None:
            nodo_actual.valor.imprimir()
            nodo_actual = nodo_actual.puntero