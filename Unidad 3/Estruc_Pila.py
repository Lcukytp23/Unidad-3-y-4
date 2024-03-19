class Pila:
    def __init__(self, capacidad_maxima):
        self.items = []
        self.tope = 0
        self.capacidad_maxima = capacidad_maxima

    def insertar(self, elemento):
        if self.tope < self.capacidad_maxima:
            self.items.append(elemento)
            self.tope += 1
            print(f"Insertado {elemento}. Tope ahora en {self.tope}.")
        else:
            print("Error: desbordamiento de la pila.")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.items.pop()
            self.tope -= 1
            print(f"Eliminado {elemento}. Tope ahora en {self.tope}.")
        else:
            print("Error: subdesbordamiento de la pila.")

# Crear una pila con capacidad máxima de 8 elementos
pila = Pila(8)

# a. Insertar (PILA, X)
pila.insertar('X')

# b. Insertar (PILA, Y)
pila.insertar('Y')

# c. Eliminar (PILA, Z)
pila.eliminar()

# d. Eliminar (PILA, T)
pila.eliminar()

# e. Eliminar (PILA, U)
pila.eliminar()

# f. Insertar (PILA, V)
pila.insertar('V')

# g. Insertar (PILA, W)
pila.insertar('W')

# h. Eliminar (PILA, p)
pila.eliminar()

# i. Insertar (PILA, R)
pila.insertar('R')

print(f"La pila final tiene {pila.tope} elementos.")
