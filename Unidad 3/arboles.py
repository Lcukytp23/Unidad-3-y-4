class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(valor, self.raiz)

    def _eliminar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursivo(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                nodo_actual.valor = self._min_valor(nodo_actual.derecha)
                nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.valor, nodo_actual.derecha)

        return nodo_actual

    def _min_valor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def imprimir_en_orden(self):
        self._imprimir_en_orden_recursivo(self.raiz)

    def _imprimir_en_orden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir_en_orden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self._imprimir_en_orden_recursivo(nodo_actual.derecha)


# Ejemplo de uso
arbol = Arbol()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("Imprimir en orden:")
arbol.imprimir_en_orden()

print("\nBuscar 4:", arbol.buscar(4))
print("Buscar 10:", arbol.buscar(10))

arbol.eliminar(5)
print("\nImprimir en orden después de eliminar el nodo con valor 5:")
arbol.imprimir_en_orden()
