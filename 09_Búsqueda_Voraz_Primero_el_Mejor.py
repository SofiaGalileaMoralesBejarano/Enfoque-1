Enfoque 1: Busqueda voraz primero el mejor
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código busca el camino más corto entre dos nodos en un grafo usando una heurística basada en la distancia absoluta entre nodos.

class Graph:
    def __init__(self):
        self.edges = {}  # Diccionario para guardar las conexiones entre nodos

    def add_edge(self, u, v):
        # Crea la conexión bidireccional entre dos nodos
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append(v)
        self.edges[v].append(u)  

    def get_neighbors(self, node):
        return self.edges.get(node, [])  # Devuelve los vecinos de un nodo

def heuristic(a, b):
    return abs(a - b)  # Calcula la distancia heurística entre dos nodos

class Node:
    def __init__(self, state):
        self.state = state
        self.parent = None  # Guarda el nodo anterior para reconstruir el camino

def greedy_best_first_search(graph, start, goal):
    open_set = []  # Lista de nodos por explorar
    closed_set = set()  # Conjunto de nodos ya visitados
    start_node = Node(start)
    open_set.append(start_node)

    while open_set:
        # Selecciona el nodo con menor valor heurístico hacia el objetivo
        current_node = min(open_set, key=lambda node: heuristic(node.state, goal))

        # Si se alcanza el objetivo, reconstruye el camino
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        open_set.remove(current_node)
        closed_set.add(current_node.state)

        # Explora los vecinos del nodo actual
        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue
            neighbor_node = Node(neighbor)
            if neighbor_node not in open_set:
                open_set.append(neighbor_node)
                neighbor_node.parent = current_node

    return None  # Si no se encuentra camino

# Construcción del grafo
grafo = Graph()
grafo.add_edge(1, 2)
grafo.add_edge(1, 3)
grafo.add_edge(2, 4)
grafo.add_edge(2, 5)
grafo.add_edge(3, 6)
grafo.add_edge(4, 7)
grafo.add_edge(5, 7)
grafo.add_edge(6, 7)

# Definición de inicio y objetivo
inicio = 1
objetivo = 7

# Ejecución del algoritmo
resultado = greedy_best_first_search(grafo, inicio, objetivo)

# Muestra el resultado
if resultado:
    print("Camino encontrado (por Greedy Best-First Search):", resultado)
else:
    print("No se encontró un camino.")
