from queue import Queue

def sumar_colas(cola_a, cola_b):
    if cola_a.qsize() != cola_b.qsize():
        raise ValueError("Las colas deben tener la misma longitud")

    cola_resultado = Queue()
    while not cola_a.empty() and not cola_b.empty():
        elemento_a = cola_a.get()
        elemento_b = cola_b.get()
        suma_elementos = elemento_a + elemento_b
        cola_resultado.put(suma_elementos)

    return cola_resultado

def ingresar_datos_cola():
    cola = Queue()
    while True:
        elemento = input("Ingrese un número entero (o 'fin' para terminar): ")
        if elemento.lower() in ['fin', 'end','0' ]:
            break
        try:
            elemento = int(elemento)
            cola.put(elemento)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    return cola

# Ingreso de datos para las colas
print("Ingrese los elementos para la Cola A:")
cola_a = ingresar_datos_cola()

print("Ingrese los elementos para la Cola B:")
cola_b = ingresar_datos_cola()

# Sumar colas
try:
    cola_resultado = sumar_colas(cola_a, cola_b)

    # Mostrar tabla con la cola que se está sumando
    print("\nSuma de las colas a y b:")
    while not cola_resultado.empty():
        fila = []
        if not cola_a.empty():
            fila.append(cola_a.get())

        if not cola_b.empty():
            fila.append(cola_b.get())
        fila.append(cola_resultado.get())
        print(fila)

except ValueError as e:
    print("Error:", e)

