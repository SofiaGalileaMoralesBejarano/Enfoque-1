 Enfoque 1: Heuristicas
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este programa aplica el algoritmo A*, que busca el camino más corto entre un nodo inicial y uno objetivo usando una heurística.
# Combina dos valores:
# g(n): costo real desde el inicio hasta el nodo actual.
# h(n): estimación del costo restante hasta la meta.
# Su evaluación total es f(n) = g(n) + h(n).
# En este caso, la heurística usada es la distancia absoluta entre el nodo actual y el objetivo.


# Función Heurística

def heuristic(a, b):
    # Calcula la distancia heurística (diferencia absoluta)
    return abs(a - b)

# Representa cada nodo en el grafo

class Node:
    def __init__(self, state):
        self.state = state      # Identificador del nodo (por ejemplo, número)
        self.parent = None      # Nodo padre (para reconstruir el camino)
        self.g = 0              # Costo acumulado desde el inicio
        self.h = 0              # Costo heurístico estimado al objetivo

    def f(self):
        # f(n) = g(n) + h(n): costo total estimado
        return self.g + self.h  

# Estructura de datos para representar los grafos
class Graph:
    def __init__(self):
        self.edges = {}  # Diccionario de listas para guardar conexiones

    def add_edge(self, u, v):
        # Agrega una arista dirigida del nodo u al nodo v
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)

    def get_neighbors(self, node):
        # Devuelve los nodos vecinos del nodo actual
        return self.edges.get(node, [])

# Búsqueda con heurística

def a_star(graph, start, goal):
    open_set = []       # Lista de nodos por explorar
    closed_set = set()  # Conjunto de nodos ya evaluados

    start_node = Node(start)
    goal_node = Node(goal)
    open_set.append(start_node)

    # Bucle principal de búsqueda
    while open_set:
        # Selecciona el nodo con el menor valor de f(n)
        current_node = min(open_set, key=lambda node: node.f())

        # Si se alcanza el objetivo, reconstruye el camino
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Devuelve el camino en orden correcto
        
        # Mueve el nodo actual al conjunto cerrado
        open_set.remove(current_node)
        closed_set.add(current_node.state)

        # Revisa los vecinos del nodo actual
        for neighbor in graph.get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue  # Si ya fue visitado, lo ignora

            neighbor_node = Node(neighbor)
            tentative_g = current_node.g + 1  # Costo desde el inicio

            # Si el vecino no está en open_set, lo agrega
            if neighbor_node not in open_set:
                open_set.append(neighbor_node)
            # Si el nuevo costo no mejora el anterior, salta
            elif tentative_g >= neighbor_node.g:
                continue

            # Actualiza los valores del nodo vecino
            neighbor_node.parent = current_node
            neighbor_node.g = tentative_g
            neighbor_node.h = heuristic(neighbor_node.state, goal)

    # Si no se encuentra un camino posible
    return None

# Iicio de programa
if __name__ == "__main__":
    grafo = Graph()
    # Se agregan las conexiones entre los nodos del grafo
    grafo.add_edge(1, 2)
    grafo.add_edge(1, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(2, 5)
    grafo.add_edge(3, 6)
    grafo.add_edge(4, 5)
    grafo.add_edge(5, 6)

    # Ejecuta el algoritmo A*
    resultado = a_star(grafo, 1, 6)
    print("A* - Camino encontrado:", resultado)
