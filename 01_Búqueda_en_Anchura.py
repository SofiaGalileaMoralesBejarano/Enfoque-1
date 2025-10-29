
# Enfoque 1: Busqueda en anchura
# Autor: Sofia Galilea Morales Bejarano 6°E

# Busca un camino desde un nodo inicial hasta un nodo objetivo
# revisando primero los nodos más cercanos (por niveles) usando BFS.

class Graph:
    def __init__(self):
        self.edges = {}  # Diccionario para guardar vecinos de cada nodo

    def add_edge(self, u, v):
        # Si el nodo u no está en el grafo, lo creo con lista vacía
        if u not in self.edges:
            self.edges[u] = []
        # Agrego v como vecino de u
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Devuelvo los vecinos del nodo, o lista vacía si no tiene
        return self.edges.get(node, [])

def bfs(graph, start, goal):
    queue = [(start, [start])]  # Cola con tuplas (nodo actual, camino hasta él)
    visited = set()  # Conjunto de nodos visitados

    while queue:
        (vertex, path) = queue.pop(0)  # Tomo el primer elemento de la cola

        if vertex in visited:  # Si ya fue visitado, salto
            continue

        visited.add(vertex)  # Marco como visitado

        for neighbor in graph.get_neighbors(vertex):  # Recorro vecinos
            if neighbor == goal:  # Si es el objetivo, retorno camino
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))  # Agrego vecino a la cola

    return None  # Si no se encuentra camino

if __name__ == "__main__":
    grafo = Graph()  # Creo el grafo
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 7)

    resultado = bfs(grafo, 1, 5)  # Busco camino desde 1 hasta 5
    print("Camino encontrado en busqueda en anchura:", resultado)
