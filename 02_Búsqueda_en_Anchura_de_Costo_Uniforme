# Enfoque 1: Busqueda en anchura de costo uniforme
# Autor: Sofia Galilea Morales Bejarano 6°E

# El objetivo de este programa es encontrar la ruta más corta desde un nodo inicial hasta un nodo objetivo dentro de un grafo.

class Graph:
    def __init__(self):
        # Creo un diccionario donde cada nodo tendrá una lista de vecinos
        self.edges = {}

    def add_edge(self, u, v):
        # Si el nodo u no está en el grafo, lo agrego con una lista vacía
        if u not in self.edges:
            self.edges[u] = []
        # Agrego v a la lista de nodos conectados con u
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Devuelvo los vecinos del nodo (si no tiene, regreso lista vacía)
        return self.edges.get(node, [])

def bfs(graph, start, goal):
    # La cola guarda tuplas (nodo actual, camino recorrido)
    queue = [(start, [start])]
    # Conjunto para guardar los nodos ya visitados y no repetirlos
    visited = set()

    # Mientras la cola no esté vacía
    while queue:
        # Saco el primer nodo de la cola (orden FIFO)
        (vertex, path) = queue.pop(0)

        # Si ya visité este nodo, lo salto
        if vertex in visited:
            continue

        # Marco el nodo como visitado
        visited.add(vertex)

        # Recorro los vecinos del nodo actual
        for neighbor in graph.get_neighbors(vertex):
            # Si el vecino es el objetivo, devuelvo el camino completo
            if neighbor == goal:
                return path + [neighbor]
            # Si no, lo meto a la cola con el nuevo camino acumulado
            queue.append((neighbor, path + [neighbor]))

    # Si termino el while sin encontrar el objetivo, regreso None
    return None

if __name__ == "__main__":
    grafo = Graph()  # Creo el grafo
    grafo.add_edge(1, 2)  # 1 se conecta con 2
    grafo.add_edge(1, 3)  # 1 se conecta con 3
    grafo.add_edge(2, 4)  # 2 se conecta con 4
    grafo.add_edge(2, 5)  # 2 se conecta con 5
    grafo.add_edge(3, 6)  # 3 se conecta con 6
    grafo.add_edge(4, 7)  # 4 se conecta con 7

    # Busco el camino desde el nodo 1 hasta el nodo 5
    resultado = bfs(grafo, 1, 5)

    # Imprimo el resultado. Debería salir [1, 2, 5]
    print("Camino en busqueda de costo uniforme:", resultado)
