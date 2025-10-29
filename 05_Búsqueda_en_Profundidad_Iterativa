# Enfoque 1: Busqueda en profundidad iterativa
# Autor: Sofia Galilea Morales Bejarano

# Similar en la búsqueda en anchura (BFS) y la profundidad (DFS). Básicamente, hace varias búsquedas en profundidad pero aumentando el límite cada vez. 

class Graph:
    def __init__(self):
        # Diccionario donde guardo los nodos y sus vecinos
        self.edges = {}

    def add_edge(self, u, v):
        # Si el nodo u no existe todavía, lo agrego con lista vacía
        if u not in self.edges:
            self.edges[u] = []
        # Agrego el nodo v como vecino de u (creo la conexión)
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Devuelvo la lista de vecinos del nodo, o vacía si no tiene
        return self.edges.get(node, [])

def ids(graph, start, goal):
    # Defino una función interna para hacer la búsqueda con límite
    def dls(node, goal, limit):
        # Si ya se acabó el límite, no sigo bajando
        if limit < 0:
            return None
        # Si el nodo actual es el que busco, lo regreso como lista
        if node == goal:
            return [node]
        # Recorro los vecinos del nodo actual
        for neighbor in graph.get_neighbors(node):
            # Llamada recursiva con el límite disminuido
            path = dls(neighbor, goal, limit - 1)
            # Si la llamada encontró un camino, lo devuelvo agregando el actual
            if path is not None:
                return [node] + path
        # Si no se encontró nada en este nivel, regreso None
        return None

    # Empiezo con profundidad 0 e incremento poco a poco
    depth = 0
    while True:
        # Llamo la búsqueda limitada con la profundidad actual
        path = dls(start, goal, depth)
        # Si ya se encontró un camino, lo regreso
        if path is not None:
            return path
        # Si no, aumento el límite y pruebo otra vez
        depth += 1

if __name__ == "__main__":
    grafo = Graph()  # Creo el grafo
    grafo.add_edge(1, 2)  # 1 se conecta con 2
    grafo.add_edge(1, 3)  # 1 se conecta con 3
    grafo.add_edge(2, 4)  # 2 se conecta con 4
    grafo.add_edge(2, 5)  # 2 se conecta con 5
    grafo.add_edge(3, 6)  # 3 se conecta con 6
    grafo.add_edge(4, 7)  # 4 se conecta con 7

    # Busco el camino desde el nodo 1 hasta el nodo 5 con búsqueda iterativa
    resultado = ids(grafo, 1, 5)

    # Imprimo el resultado, debería salir [1, 2, 5]
    print("Camino encontrado en busqueda en profundidad iterativa:", resultado)
