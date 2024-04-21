def floyd_warshall(graph):
    # Inicializar la matriz de distancias con las distancias directas entre los vértices
    distances = {i: {j: float('infinity') for j in graph} for i in graph}
    for i in graph:
        distances[i][i] = 0
        for neighbor, weight in graph[i].items():
            distances[i][neighbor] = weight
    
    # Calcular los caminos más cortos
    for k in graph:
        for i in graph:
            for j in graph:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 3, 'C': 8},
    'B': {'A': 3, 'C': 1},
    'C': {'A': 8, 'B': 1}
}
distances = floyd_warshall(graph)
print("Matriz de distancias:")
for i in graph:
    print(i, distances[i])
