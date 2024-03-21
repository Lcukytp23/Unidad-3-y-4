class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor):
        nuevo_nodo = NodoCola(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor

    def ver_primero(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.primero.valor

    def __str__(self):
        valores = []
        nodo_actual = self.primero
        while nodo_actual:
            valores.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return str(valores)

# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Cola actual:", cola)
print("Primero de la cola:", cola.ver_primero())
print("Desencolando:", cola.desencolar())
print("Cola después de desencolar:", cola)
