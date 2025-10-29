 Enfoque 1: Busqueda de haz local
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código implementa la búsqueda en haz (beam search), que explora múltiples estados a la vez, 
# genera vecinos para cada uno y conserva solo los mejores según su evaluación en cada iteración.

class LocalBeamSearch:
    def __init__(self, initial_states, evaluate, neighbors, beam_width):
        self.beam_width = beam_width            # Cantidad de estados a mantener
        self.current_states = initial_states    # Estados actuales en el haz
        self.evaluate = evaluate                # Función para evaluar estados
        self.neighbors = neighbors              # Función para generar vecinos

    def search(self, iterations):
        for _ in range(iterations):
            all_neighbors = []
            # Genero todos los vecinos de los estados actuales
            for state in self.current_states:
                all_neighbors.extend(self.neighbors(state))
            all_neighbors = list(set(all_neighbors))  # Elimino duplicados

            # Evalúo los vecinos y los ordeno de mejor a peor
            scored_neighbors = [(state, self.evaluate(state)) for state in all_neighbors]
            scored_neighbors.sort(key=lambda x: x[1], reverse=True)

            # Mantengo solo los mejores según el ancho del haz
            self.current_states = [state for state, _ in scored_neighbors[:self.beam_width]]

        # Retorno el mejor estado encontrado
        return max(self.current_states, key=self.evaluate)

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def get_neighbors(self, state):
        # Genera vecinos sumando o restando 1
        return [state + i for i in [-1, 1]]  

    def evaluate(self, state):
        # Valor a maximizar: cuanto más cerca de 0, mejor
        return -abs(state) 

initial_states = [0, 1]  # Estados iniciales del haz
beam_width = 2            # Tamaño del haz
iterations = 10           # Número de iteraciones

problem = Problem(initial_state=0)

# Creo el objeto de búsqueda y ejecuto
local_beam_search = LocalBeamSearch(initial_states, problem.evaluate, problem.get_neighbors, beam_width)
best_solution = local_beam_search.search(iterations)

# Imprimo la mejor solución y su valor
print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", problem.evaluate(best_solution))
