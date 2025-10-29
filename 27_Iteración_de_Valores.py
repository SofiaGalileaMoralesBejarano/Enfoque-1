Enfoque 1: Iteracion de valores
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Este código aplica el algoritmo de iteración de valores para un proceso de decisión de Markov (MDP), calculando la función de valor óptima asociada a cada estado.


# Inicio:

class ValueIteration:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities  # P(s'|s,a)
        self.rewards = rewards                                      # R(s,a,s')
        self.discount_factor = discount_factor                      # Factor de descuento gamma
        self.value_function = {state: 0 for state in states}        # Inicialización de la función de valor

    def iterate(self, threshold):
        while True:
            delta = 0
            for state in self.states:
                v = self.value_function[state]
                # Actualiza el valor del estado con el máximo valor sobre todas las acciones
                self.value_function[state] = max(self.calculate_action_value(state, action) for action in self.actions)
                delta = max(delta, abs(v - self.value_function[state]))
            # Si el cambio máximo es menor que el umbral, terminamos la iteración
            if delta < threshold:
                break

    def calculate_action_value(self, state, action):
        # Calcula el valor esperado de tomar una acción en un estado considerando transiciones y recompensas
        return sum(
            self.transition_probabilities[state][action][next_state] * 
            (self.rewards[state][action][next_state] + self.discount_factor * self.value_function[next_state]) 
            for next_state in self.states
        )

if __name__ == "__main__":
    states = ['s1', 's2']
    actions = ['a1', 'a2']
    
    # Probabilidades de transición: P(s' | s, a)
    transition_probabilities = {
        's1': {'a1': {'s1': 0.8, 's2': 0.2}, 'a2': {'s1': 0.5, 's2': 0.5}},
        's2': {'a1': {'s1': 0.1, 's2': 0.9}, 'a2': {'s1': 0.3, 's2': 0.7}}
    }
    
    # Recompensas: R(s, a, s')
    rewards = {
        's1': {'a1': {'s1': 5, 's2': 10}, 'a2': {'s1': 1, 's2': 2}},
        's2': {'a1': {'s1': 0, 's2': 3}, 'a2': {'s1': 4, 's2': 1}}
    }
    
    discount_factor = 0.9
    threshold = 0.01

    vi = ValueIteration(states, actions, transition_probabilities, rewards, discount_factor)
    vi.iterate(threshold)

    # Imprime la función de valor final para cada estado
    print("Funciones de valor finales:", vi.value_function)
