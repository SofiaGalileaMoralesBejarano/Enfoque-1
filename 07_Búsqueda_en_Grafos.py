Enfoque 1: Busqueda en grafos
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este programa permite buscar caminos en un grafo usando dos métodos:
# BFS (Búsqueda en anchura): recorre los nodos por niveles, empezando por los más cercanos al origen.
# DFS (Búsqueda en profundidad): explora un camino completo antes de retroceder.
# El usuario elige el método deseado al llamar la función graph_search('bfs') o graph_search('dfs').

class Graph:
    def __init__(self):
        # Diccionario donde cada nodo tiene su lista de vecinos
        self.edges = {}

    def add_edge(self, u, v):
        # Agrega una arista dirigida del nodo u al nodo v
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Devuelve los nodos vecinos conectados al nodo actual
        return self.edges.get(node, [])

def graph_search(graph, start, goal, strategy='bfs'):
    # Según la estrategia seleccionada, usa BFS o DFS
    if strategy == 'bfs':
        return bfs(graph, start, goal)
    elif strategy == 'dfs':
        return dfs(graph, start, goal)

# ============================================================
# BUSQUEDA EN ANCHURA (BFS)
# ============================================================
def bfs(graph, start, goal):
    queue = [(start, [start])]  # Cola con tuplas (nodo_actual, camino)
    visited = set()  # Conjunto de nodos ya visitados

    while queue:
        (vertex, path) = queue.pop(0)  # Saca el primer elemento (FIFO)

        if vertex in visited:
            continue  # Si ya lo visité, paso al siguiente

        visited.add(vertex)  # Marco el nodo como visitado

        if vertex == goal:
            return path  # Si llegué al objetivo, regreso el camino

        # Agrego los vecinos del nodo actual a la cola
        for neighbor in graph.get_neighbors(vertex):
            queue.append((neighbor, path + [neighbor]))

    return None  # Si no se encontró un camino

# Búsqueda en profundidad
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)  # Marco el nodo como visitado

    if start == goal:
        return [start]  # Si llegué al objetivo, regreso el nodo

    # Recorro los vecinos no visitados
    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            if path is not None:
                return [start] + path  # Armo el camino de regreso
    return None

# Inicio del programa
if __name__ == "__main__":
    grafo = Graph()
    # Se agregan las conexiones entre los nodos (grafo dirigido)
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 5)
    grafo.add_edge(5, 6)

    # Ejecuto búsqueda en anchura (BFS)
    resultado_bfs = graph_search(grafo, 1, 6, strategy='bfs')
    print("Búsqueda en anchura (BFS) - Camino encontrado:", resultado_bfs)

    # Ejecuto búsqueda en profundidad (DFS)
    resultado_dfs = graph_search(grafo, 1, 6, strategy='dfs')
    print("Búsqueda en profundidad (DFS) - Camino encontrado:", resultado_dfs)
