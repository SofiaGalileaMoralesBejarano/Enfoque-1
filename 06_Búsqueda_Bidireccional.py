# Enfoque 1: Busqueda bidireccional
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:
# Este programa implementa la búsqueda bidireccional, que busca un camino desde el nodo inicial hasta el nodo objetivo empezando desde ambos extremos al mismo tiempo. 
class Graph:
    def __init__(self):
        # Diccionario donde cada nodo tiene una lista de vecinos
        self.edges = {}

    def add_edge(self, u, v):
        # Si el nodo u o v no existen, los creo con lista vacía
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        # Conecto u con v y v con u (grafo no dirigido)
        self.edges[u].append(v)
        self.edges[v].append(u)

    def get_neighbors(self, node):
        # Devuelvo la lista de vecinos del nodo, o vacía si no tiene
        return self.edges.get(node, [])

def bidirectional_search(graph, start, goal):
    # Si el nodo inicial es el mismo que el objetivo, regreso solo ese nodo
    if start == goal:
        return [start]

    # Conjuntos de nodos visitados desde el inicio y desde el objetivo
    visited_start = {start}
    visited_goal = {goal}

    # Colas para ir explorando desde ambos extremos, guardando caminos
    queue_start = [(start, [start])]
    queue_goal = [(goal, [goal])]

    # Mientras haya nodos por explorar desde ambos lados
    while queue_start and queue_goal:

        # Reviso el siguiente nodo desde el inicio
        path_start, current_start = queue_start.pop(0)

        # Si este nodo ya fue visitado desde el objetivo, se encontraron
        if current_start in visited_goal:
            for path_goal, current_goal in queue_goal:
                if current_goal == current_start:
                    # Combino ambos caminos y regreso
                    return path_start + path_goal[::-1][1:]

        # Recorro los vecinos desde el inicio
        for neighbor in graph.get_neighbors(current_start):
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append((path_start + [neighbor], neighbor))

        # Reviso el siguiente nodo desde el objetivo
        path_goal, current_goal = queue_goal.pop(0)

        # Si este nodo ya fue visitado desde el inicio, se encontraron
        if current_goal in visited_start:
            for path_start, current_start in queue_start:
                if current_start == current_goal:
                    # Combino ambos caminos y regreso
                    return path_goal + path_start[::-1][1:]

        # Recorro los vecinos desde el objetivo
        for neighbor in graph.get_neighbors(current_goal):
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append((path_goal + [neighbor], neighbor))

    # Si no se encuentra el camino, regreso None
    return None

if __name__ == "__main__":

    grafo = Graph()  # Creo el grafo
    grafo.add_edge(1, 2)  # Conecto 1 con 2
    grafo.add_edge(1, 3)  # Conecto 1 con 3
    grafo.add_edge(2, 4)  # Conecto 2 con 4
    grafo.add_edge(2, 5)  # Conecto 2 con 5
    grafo.add_edge(3, 6)  # Conecto 3 con 6
    grafo.add_edge(4, 5)  # Conecto 4 con 5
    grafo.add_edge(5, 6)  # Conecto 5 con 6

    # Busco el camino desde el nodo 1 hasta el 6 usando búsqueda bidireccional
    resultado = bidirectional_search(grafo, 1, 6)

    # Imprimo el camino encontrado
    print("Camino encontrado:", resultado)
