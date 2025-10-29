Enfoque 1: Algoritmos geneticos
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código usa un algoritmo genético que busca la mejor solución mediante una población de individuos, aplicando selección, cruce y mutación a lo largo de varias generaciones.

import random

class GeneticAlgorithm:
    def __init__(self, population_size, mutate_rate, crossover_rate, evaluate, mutate, crossover):
        self.population_size = population_size  # Tamaño de la población
        self.mutate_rate = mutate_rate          # Probabilidad de mutación
        self.crossover_rate = crossover_rate    # Probabilidad de cruce
        self.evaluate = evaluate                # Función de evaluación
        self.mutate = mutate                    # Función de mutación
        self.crossover = crossover              # Función de cruce

    def run(self, generations):
        population = self.initialize_population()  # Creo población inicial

        for _ in range(generations):
            # Ordeno la población de mejor a peor
            population = sorted(population, key=self.evaluate, reverse=True)
            next_generation = population[:2]  # Mantengo los dos mejores

            # Genero nuevos individuos hasta completar la población
            while len(next_generation) < self.population_size:
                # Selecciono padres entre los mejores 10
                parent1, parent2 = random.choices(population[:10], k=2)
                
                # Aplico cruce según la probabilidad
                if random.random() < self.crossover_rate:
                    child = self.crossover(parent1, parent2)
                else:
                    child = parent1
                
                # Aplico mutación según la probabilidad
                if random.random() < self.mutate_rate:
                    child = self.mutate(child)

                next_generation.append(child)

            population = next_generation  # Actualizo la población

        # Retorno el mejor individuo de la última generación
        return max(population, key=self.evaluate)

    def initialize_population(self):
        # Genera la población inicial de forma aleatoria
        return [self.random_solution() for _ in range(self.population_size)]

    def random_solution(self):
        # Solución aleatoria en el rango 0-100
        return random.randint(0, 100)  
    
# Función de evaluación: mientras mayor el valor, mejor
def evaluate(solution):
    return solution  

# Función de mutación: cambia ligeramente el valor
def mutate(solution):
    return solution + random.randint(-5, 5)

# Función de cruce: promedio de los padres
def crossover(parent1, parent2):
    return (parent1 + parent2) // 2

# Parámetros del algoritmo
population_size = 20
mutate_rate = 0.2
crossover_rate = 0.7
generations = 50

# Creo el objeto y ejecuto el algoritmo
ga = GeneticAlgorithm(population_size, mutate_rate, crossover_rate, evaluate, mutate, crossover)
best_solution = ga.run(generations)

# Imprimo la mejor solución y su valor
print("Mejor solución encontrada:", best_solution)
print("Valor de la mejor solución:", evaluate(best_solution))

