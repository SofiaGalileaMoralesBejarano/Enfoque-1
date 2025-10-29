Enfoque 1: Busqueda de temple simulado
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código implementa recocido simulado (simulated annealing), que busca una solución óptima explorando vecinos y, 
# ocasionalmente, aceptando soluciones peores con una probabilidad decreciente, para evitar quedar atrapado en óptimos locales.

import random
import math

class SimulatedAnnealing:
    def __init__(self, initial_solution, evaluate, neighbors):
        self.current_solution = initial_solution  # Solución actual
        self.current_value = evaluate(initial_solution)  # Valor de la solución actual
        self.evaluate = evaluate                    # Función de evaluación
        self.neighbors = neighbors                  # Función para generar vecinos

    def anneal(self, initial_temp, cooling_rate, stopping_temp):
        temperature = initial_temp  # Temperatura inicial
        best_solution = self.current_solution
        best_value = self.current_value
        
        while temperature > stopping_temp:
            # Elijo un vecino aleatorio
            neighbor = random.choice(self.neighbors(self.current_solution))
            neighbor_value = self.evaluate(neighbor)

            # Si el vecino es mejor o se acepta por probabilidad según la temperatura
            if neighbor_value > self.current_value or random.uniform(0, 1) < math.exp((neighbor_value - self.current_value) / temperature):
                self.current_solution = neighbor
                self.current_value = neighbor_value
        
            # Actualizo la mejor solución encontrada
            if self.current_value > best_value:
                best_solution = self.current_solution
                best_value = self.current_value

            temperature *= cooling_rate  # Enfriamiento gradual
        
        return best_solution  # Retorna la mejor solución encontrada

# Función de evaluación: valor a maximizar
def evaluate(solution):
    return -(solution**2) + 10  # Máximo en solution = 0

# Genera vecinos cercanos para explorar
def neighbors(solution):
    return [solution + i for i in [-1, 1, -2, 2]]  

initial_solution = 0  # Solución inicial

# Parámetros del temple simulado
initial_temp = 1000    # Temperatura inicial
cooling_rate = 0.95    # Tasa de enfriamiento
stopping_temp = 1      # Temperatura de parada

# Creo el objeto y ejecuto el algoritmo
simulated_annealing = SimulatedAnnealing(initial_solution, evaluate, neighbors)
best_solution = simulated_annealing.anneal(initial_temp, cooling_rate, stopping_temp)

# Imprimo los resultados
print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", evaluate(best_solution))
