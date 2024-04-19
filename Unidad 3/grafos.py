import networkx as nx
import matplotlib.pyplot as plt

estados = {
    'Aguascalientes': {'Zacatecas': 200, 'Jalisco': 300},
    'Zacatecas': {'Aguascalientes': 200, 'Jalisco': 250, 'Durango': 400},
    'Jalisco': {'Aguascalientes': 300, 'Zacatecas': 250, 'Colima': 150},
    'Durango': {'Zacatecas': 400, 'Coahuila': 500},
    'Colima': {'Jalisco': 150, 'Michoacán': 200},
    'Michoacán': {'Colima': 200, 'Guanajuato': 300},
    'Guanajuato': {'Michoacán': 300, 'Jalisco': 350}
}


G = nx.Graph()

for estado in estados:
    G.add_node(estado)

for estado, vecinos in estados.items():
    for vecino, distancia in vecinos.items():
        G.add_edge(estado, vecino, weight=distancia)

pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo de los Estados de México con sus Relaciones')
plt.show()

def calcular_costo_recorrido(recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        costo_total += estados[recorrido[i]][recorrido[i+1]]
    return costo_total


recorrido_sin_repetir = nx.shortest_path(G, source='Aguascalientes', target='Guanajuato')
print("Recorrido sin repetir ningún estado:", recorrido_sin_repetir)
print("Costo total del recorrido sin repetir ningún estado:", calcular_costo_recorrido(recorrido_sin_repetir))

recorrido_con_repetición = nx.eulerian_circuit(G, source='Aguascalientes')
recorrido_con_repetición = [node for node, _ in recorrido_con_repetición]
recorrido_con_repetición.append(recorrido_con_repetición[0]) 
print("Recorrido con repeticiones de al menos un estado:", recorrido_con_repetición)
print("Costo total del recorrido con repeticiones de al menos un estado:", calcular_costo_recorrido(recorrido_con_repetición))
