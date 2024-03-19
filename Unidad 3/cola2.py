from queue import Queue

class SeguroApp:
    def __init__(self):
        self.colas = {}

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = Queue()
        num_atencion = self.colas[servicio].qsize() + 1
        self.colas[servicio].put(num_atencion)
        return num_atencion

    def atender_cliente(self, servicio):
        if servicio in self.colas and not self.colas[servicio].empty():
            num_atencion = self.colas[servicio].get()
            return num_atencion
        else:
            return None

# Función principal
def main():
    app = SeguroApp()

    while True:
        opcion = input("Ingrese 'C' para llegada de cliente, 'A' para atención, o 'Q' para salir: ").strip().upper()

        if opcion == 'Q':
            print("Saliendo del programa...")
            break

        if opcion == 'C':
            servicio = input("Ingrese el número de servicio para el cliente: ").strip()
            num_atencion = app.llegada_cliente(servicio)
            print("Cliente llegado. Número de atención:", num_atencion)

        elif opcion == 'A':
            servicio = input("Ingrese el número de servicio que desea atender: ").strip()
            num_atencion = app.atender_cliente(servicio)
            if num_atencion is not None:
                print("Atendiendo cliente. Número de atención:", num_atencion)
            else:
                print("No hay clientes en espera para el servicio", servicio)

        else:
            print("Opción no válida. Por favor, ingrese 'C', 'A' o 'Q'.")

if __name__ == "__main__":
    main()
