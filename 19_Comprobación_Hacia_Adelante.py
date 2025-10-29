Enfoque 1: Comprobacion hacia delante
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo: 

# Aquí encuentra un camino en un grafo desde un nodo inicial hasta uno objetivo usando backtracking con forward checking, 
# evitando recorrer rutas que conduzcan a callejones sin salida.


class Graph:
    def __init__(self):
        self.edges = {}  # Diccionario para almacenar los vecinos de cada nodo

    def add_edge(self, u, v):
        # Si los nodos no existen, los creo con lista vacía
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        # Agrego las conexiones (grafo no dirigido)
        self.edges[u].append(v)
        self.edges[v].append(u)

    def get_neighbors(self, node):
        # Devuelvo los vecinos del nodo
        return self.edges.get(node, [])

class PathFinder:
    def __init__(self, graph):
        self.graph = graph

    def is_valid(self, node, path):
        # Verifico que el nodo no esté ya en el camino
        return node not in path

    def forward_check(self, node, path):
        # Comprueba si al avanzar desde este nodo queda algún vecino válido
        for neighbor in self.graph.get_neighbors(node):
            if self.is_valid(neighbor, path):
                return True
        return False

    def backtrack(self, current_node, goal, path):
        path.append(current_node)  # Agrego el nodo actual al camino

        if current_node == goal:
            return path  # Objetivo alcanzado

        for neighbor in self.graph.get_neighbors(current_node):
            # Solo avanzo si el vecino no está en el camino y pasa el forward check
            if self.is_valid(neighbor, path) and self.forward_check(neighbor, path):
                result = self.backtrack(neighbor, goal, path)
                if result:
                    return result
        
        path.pop()  # Retrocedo si no encuentro camino válido
        return None

    def find_path(self, start, goal):
        # Inicio la búsqueda desde el nodo inicial
        return self.backtrack(start, goal, [])

# Creo el grafo y agrego las conexiones
grafo = Graph()
grafo.add_edge(1, 2)
grafo.add_edge(1, 3)
grafo.add_edge(2, 4)
grafo.add_edge(2, 5)
grafo.add_edge(3, 6)
grafo.add_edge(4, 7)
grafo.add_edge(5, 7)
grafo.add_edge(6, 7)

# Busco el camino desde inicio hasta objetivo
path_finder = PathFinder(grafo)
inicio = 1
objetivo = 7
resultado = path_finder.find_path(inicio, objetivo)

# Imprimo el resultado
if resultado:
    print(f"Camino encontrado: {resultado}")
else:
    print("No se encontró un camino.")
