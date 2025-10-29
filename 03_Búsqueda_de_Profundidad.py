# Enfoque 1: Busqueda de profundidad
# Autor: Sofia Galilea Morales Bejarano 6°E

# En este programa se usa la búsqueda en profundidad (DFS),
# la cual explora un camino hasta el fondo antes de retroceder.
# Sirve para encontrar una ruta desde un nodo inicial hasta uno
# objetivo dentro de un grafo, recorriendo los caminos de forma
# recursiva (o sea, que la función se llama a sí misma).

class Graph:
    def __init__(self):
        # Diccionario donde cada nodo tiene su lista de vecinos
        self.edges = {}

    def add_edge(self, u, v):
        # Si el nodo u no existe todavía, lo creo con lista vacía
        if u not in self.edges:
            self.edges[u] = []
        # Agrego el nodo v a los vecinos de u (la conexión)
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Regreso los vecinos del nodo (si no tiene, devuelvo lista vacía)
        return self.edges.get(node, [])

def dfs(graph, start, goal, visited=None):
    # Si es la primera vez que entro a la función, creo el conjunto de visitados
    if visited is None:
        visited = set()

    # Marco el nodo actual como visitado
    visited.add(start)

    # Si el nodo actual es el objetivo, ya encontré el camino
    if start == goal:
        return [start]

    # Recorro los vecinos del nodo actual
    for neighbor in graph.get_neighbors(start):
        # Si el vecino no ha sido visitado, lo exploro (llamada recursiva)
        if neighbor not in visited:
            path = dfs(graph, neighbor, goal, visited)
            # Si la llamada encontró un camino, lo regreso sumando el actual
            if path is not None:
                return [start] + path

    # Si no encuentro el camino en este recorrido, regreso None
    return None

if __name__ == "__main__":
    grafo = Graph()  # Creo el grafo
    grafo.add_edge(1, 2)  # 1 se conecta con 2
    grafo.add_edge(1, 3)  # 1 se conecta con 3
    grafo.add_edge(2, 4)  # 2 se conecta con 4
    grafo.add_edge(2, 5)  # 2 se conecta con 5
    grafo.add_edge(3, 6)  # 3 se conecta con 6
    grafo.add_edge(4, 7)  # 4 se conecta con 7

    # Busco el camino desde el nodo 1 hasta el 5 usando DFS
    resultado = dfs(grafo, 1, 5)

    # Imprimo el resultado, debería salir [1, 2, 5]
    print("Camino encontrado en busqueda en profundidad:", resultado)
