Enfoque 1: Busqueda online
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:
# Este código realiza una búsqueda en línea, en la que el agente decide paso a paso desde el estado inicial, sin conocer todo el entorno, hasta llegar al objetivo.

import random

class OnlineSearch:
    def __init__(self, initial_state):
        self.initial_state = initial_state  # Estado inicial del agente

    def search(self, problem):
        current_state = self.initial_state
        path = [current_state]  # Registro del camino recorrido

        while not problem.is_goal(current_state):
            # Elijo la siguiente acción de manera heurística o aleatoria
            action = self.get_next_action(current_state)
            # Aplico la acción y actualizo el estado
            current_state = problem.perform_action(current_state, action)
            path.append(current_state)

        return path  # Retorno el camino completo hasta el objetivo

    def get_next_action(self, state):
        # Devuelve una acción disponible (aquí de forma aleatoria)
        return random.choice(['action1', 'action2'])

class Problem:
    def __init__(self, goal_state):
        self.goal_state = goal_state  # Estado objetivo

    def is_goal(self, state):
        # Comprueba si el estado actual es el objetivo
        return state == self.goal_state

    def perform_action(self, state, action):
        # Aplica la acción al estado actual
        if action == 'action1':
            return state + 1  
        elif action == 'action2':
            return state - 1  

initial_state = 0
goal_state = 5  

problem = Problem(goal_state)

# Creo el agente y realizo la búsqueda
search = OnlineSearch(initial_state)
path = search.search(problem)

# Imprimo el camino recorrido y el estado final alcanzado
print("Camino encontrado:", path)
print("Estado final alcanzado:", path[-1])
