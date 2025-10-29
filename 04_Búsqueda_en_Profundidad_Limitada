Enfoque 1: Busqueda en profundidad limitada
# Autor: Sofia Galilea Morales Bejarano 6°E

# En este programa se realiza una búsqueda en profundidad limitada, con un límite de niveles a los que se puede bajar.

class Graph: 
    def __init__(self):
        # Diccionario donde cada nodo tiene una lista con sus vecinos
        self.edges = {}

    def add_edge(self, u, v):
        # Si el nodo u no existe todavía, lo creo con lista vacía
        if u not in self.edges:
            self.edges[u] = []
        # Agrego el nodo v a los vecinos de u (la conexión)
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Devuelvo los vecinos del nodo, si no tiene regreso una lista vacía
        return self.edges.get(node, [])

def dls(graph, node, goal, limit, visited=None):
    # Si es la primera llamada, creo el conjunto de visitados
    if visited is None:
        visited = set()

    # Si el límite ya se acabó, regreso None (ya no puedo seguir bajando)
    if limit < 0:
        return None

    # Marco el nodo actual como visitado
    visited.add(node)

    # Si el nodo actual es el que busco, regreso una lista con ese nodo
    if node == goal:
        return [node]

    # Recorro los vecinos del nodo actual
    for neighbor in graph.get_neighbors(node):
        # Si el vecino no ha sido visitado, sigo explorando con un límite menos
        if neighbor not in visited:
            path = dls(graph, neighbor, goal, limit - 1, visited)
            # Si la función recursiva encontró un camino, lo devuelvo sumando el actual
            if path is not None:
                return [node] + path

    # Si no se encontró el camino dentro del límite, regreso None
    return None

def depth_limited_search(graph, start, goal, limit):
    # Esta función solo llama a dls con los valores iniciales
    return dls(graph, start, goal, limit)

if __name__ == "__main__":
    grafo = Graph()  # Creo el grafo
    grafo.add_edge(1, 2)  # 1 se conecta con 2
    grafo.add_edge(1, 3)  # 1 se conecta con 3
    grafo.add_edge(2, 4)  # 2 se conecta con 4
    grafo.add_edge(2, 5)  # 2 se conecta con 5
    grafo.add_edge(3, 6)  # 3 se conecta con 6
    grafo.add_edge(4, 7)  # 4 se conecta con 7

    # Defino el límite de profundidad (cuántos niveles puede explorar)
    limite = 2  

    # Busco el camino desde el nodo 1 hasta el nodo 5 con el límite dado
    resultado = depth_limited_search(grafo, 1, 5, limite)

    # Imprimo el resultado, debería salir [1, 2, 5]
    print("Camino encontrado en busqueda en profundidad limitada:", resultado)
