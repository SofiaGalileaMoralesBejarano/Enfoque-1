Enfoque 1: Busquedas de ascension de colinas
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código aplica una búsqueda local que parte de un estado inicial y avanza hacia el vecino con mejor valor, deteniéndose cuando ya no hay mejoras posibles.

import random

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state  # Estado inicial del problema

    def get_neighbors(self, state):
        # Genera vecinos del estado actual (un valor menor y uno mayor)
        return [state - 1, state + 1]

    def evaluate(self, state):
        # Función de evaluación: mayor valor = mejor estado
        # Aquí buscamos que el valor absoluto sea mínimo
        return -abs(state)  

def hill_climbing(problem):
    current = problem.initial_state  # Comienzo desde el estado inicial
    while True:
        neighbors = problem.get_neighbors(current)  # Obtengo los vecinos
        if not neighbors:
            return current  # Si no hay vecinos, termino
        # Selecciono el vecino con mejor evaluación
        next_state = max(neighbors, key=lambda state: problem.evaluate(state))
        # Si no mejora, termino
        if problem.evaluate(next_state) <= problem.evaluate(current):
            return current
        current = next_state  # Muevo al vecino mejor evaluado

if __name__ == "__main__":
    initial_state = random.randint(-10, 10)  # Estado inicial aleatorio
    problem = Problem(initial_state)
    result = hill_climbing(problem)
    print(f"Estado inicial: {initial_state}, Estado óptimo encontrado: {result}")
