Enfoque 1: Busqueda tabu
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código implementa la búsqueda tabú, que busca la mejor solución evitando repetir estados recientes mediante una lista tabú, mientras explora los vecinos para mejorar la solución actual.

class TabuSearch:
    def __init__(self, initial_solution, evaluate, neighbors, tabu_size=5):
        self.best_solution = initial_solution       # Mejor solución encontrada
        self.best_value = evaluate(initial_solution) # Valor de la mejor solución
        self.tabu_list = []                         # Lista tabú para evitar ciclos
        self.evaluate = evaluate                    # Función de evaluación
        self.neighbors = neighbors                  # Función para generar vecinos
        self.tabu_size = tabu_size                  # Tamaño máximo de la lista tabú

    def search(self, iterations):
        current_solution = self.best_solution       # Comienzo con la solución inicial
        for _ in range(iterations):
            neighbor_solutions = self.neighbors(current_solution)  # Obtengo vecinos
            best_neighbor = None
            best_value = float('-inf')

            # Recorro los vecinos y elijo el mejor que no esté en la lista tabú
            for neighbor in neighbor_solutions:
                if neighbor in self.tabu_list:
                    continue
                value = self.evaluate(neighbor)
                if value > best_value:
                    best_value = value
                    best_neighbor = neighbor
            
            if best_neighbor is not None:
                current_solution = best_neighbor
                # Actualizo la mejor solución si el vecino es mejor
                if self.evaluate(current_solution) > self.best_value:
                    self.best_solution = current_solution
                    self.best_value = self.evaluate(current_solution)

                # Agrego la solución actual a la lista tabú y mantengo su tamaño
                self.tabu_list.append(current_solution)
                if len(self.tabu_list) > self.tabu_size:
                    self.tabu_list.pop(0)

        return self.best_solution  # Retorno la mejor solución encontrada

# Función de evaluación: mientras más cerca de 0, mejor
def evaluate(solution):
    return -abs(solution) 

# Genera vecinos incrementando o decrementando la solución
def neighbors(solution):
    return [solution + i for i in [-1, 1]] 

initial_solution = 0  # Solución inicial

# Creo el objeto de búsqueda tabú
tabu_search = TabuSearch(initial_solution, evaluate, neighbors)

iterations = 10
best_solution = tabu_search.search(iterations)

# Imprimo la mejor solución y su valor
print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", evaluate(best_solution))
