POSTRES = {
    "Pastel de chocolate": ["harina", "azúcar", "chocolate", "huevos", "mantequilla"],
    "Tarta de manzana": ["harina", "azúcar", "manzanas", "canela", "mantequilla"],
    "Helado de vainilla": ["leche", "nata", "azúcar", "vainilla"],
    "Brownie": ["harina", "azúcar", "chocolate", "huevos", "nueces"],
}

def imprimir_ingredientes(nombre):
    if nombre in POSTRES:
        print(f'Los ingredientes para {nombre} son: {POSTRES[nombre]}')
    else:
        print('El postre no está en la lista.')

def insertar_ingredientes(nombre, nuevos_ingredientes):
    if nombre in POSTRES:
        POSTRES[nombre].extend(nuevos_ingredientes)
        print(f'Se han insertado nuevos ingredientes en {nombre}: {POSTRES[nombre]}')
    else:
        print('El postre no está en la lista.')

def eliminar_ingrediente(nombre, ingrediente):
    if nombre in POSTRES:
        if ingrediente in POSTRES[nombre]:
            POSTRES[nombre].remove(ingrediente)
            print(f'Se ha eliminado el ingrediente {ingrediente} de {nombre}.')
        else:
            print('El ingrediente no está en la lista.')
    else:
        print('El postre no está en la lista.')

def alta_postre(nombre, ingredientes):
    if nombre not in POSTRES:
        POSTRES[nombre] = ingredientes
        print(f'Se ha dado de alta el postre {nombre} con los siguientes ingredientes: {ingredientes}')
    else:
        print('El postre ya está en la lista.')

def baja_postre(nombre):
    if nombre in POSTRES:
        del POSTRES[nombre]
        print(f'Se ha dado de baja el postre {nombre}.')
    else:
        print('El postre no está en la lista.')


imprimir_ingredientes("Brownie")
insertar_ingredientes("Brownie", ["cacao en polvo"])
eliminar_ingrediente("Tarta de manzana", "canela")
alta_postre("Cheesecake", ["galletas", "queso crema", "azúcar", "mantequilla"])
baja_postre("Helado de vainilla")
