import heapq

def dijkstra(graph, start):

    distances = {vertex: float('infinity') for vertex in graph}

    distances[start] = 0
    

    queue = [(0, start)]
    
    while queue:

        current_distance, current_vertex = heapq.heappop(queue)
        

        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
print("Distancias más cortas desde", start_vertex, ":", dijkstra(graph, start_vertex))
