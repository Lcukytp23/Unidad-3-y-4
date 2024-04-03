def eliminar_elementos_repetidos(lista1):
    postres_sin_repetidos = {}
    for lista1, ingredientes in lista1.items():
        ingredientes_sin_repetidos = list(set(ingredientes))
        postres_sin_repetidos[lista1] = ingredientes_sin_repetidos
    return postres_sin_repetidos

# Ejemplo de uso
POSTRES = {
    "Pastel de chocolate": ["harina", "azúcar", "chocolate", "huevos", "mantequilla", "chocolate"],
    "Tarta de manzana": ["harina", "azúcar", "manzanas", "canela", "mantequilla", "canela"],
    "Helado de vainilla": ["leche", "nata", "azúcar", "vainilla", "azúcar"],
    "Brownie": ["harina", "azúcar", "chocolate", "huevos", "nueces", "nueces"],
}

POSTRES = eliminar_elementos_repetidos(POSTRES)
print(POSTRES)
