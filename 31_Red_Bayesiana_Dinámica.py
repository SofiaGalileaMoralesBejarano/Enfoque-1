# Enfoque 1: Red bayesiana dinamica
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Modela un HMM (Hidden Markov Model): un sistema con estados ocultos y observaciones, 
# definido por un modelo de transición entre estados y un modelo de emisión que genera las observaciones.

# Inicio:

import numpy as np

class DynamicBayesianNetwork:
    def __init__(self, states, transition_model, emission_model):
        self.states = states
        self.transition_model = transition_model  # P(s_t+1 | s_t)
        self.emission_model = emission_model      # P(o_t | s_t)

    def predict(self, current_state):
        # Predice el siguiente estado según las probabilidades de transición
        probabilities = self.transition_model[current_state]
        next_state = np.random.choice(self.states, p=probabilities)
        return next_state

    def emit(self, current_state):
        # Genera una observación basada en el estado actual
        probabilities = self.emission_model[current_state]
        observation = np.random.choice(list(probabilities.keys()), p=list(probabilities.values()))
        return observation

if __name__ == "__main__":
    states = ['Rainy', 'Sunny']

    # Probabilidades de transición entre estados
    transition_model = {
        'Rainy': [0.7, 0.3],  # P(Rainy->Rainy)=0.7, P(Rainy->Sunny)=0.3
        'Sunny': [0.4, 0.6]   # P(Sunny->Rainy)=0.4, P(Sunny->Sunny)=0.6
    }

    # Probabilidades de emisión de observaciones según el estado
    emission_model = {
        'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5},
        'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1}
    }

    dbn = DynamicBayesianNetwork(states, transition_model, emission_model)

    current_state = 'Rainy'
    for _ in range(5): 
        next_state = dbn.predict(current_state)
        observation = dbn.emit(current_state)
        print(f"Estado actual: {current_state}, Estado siguiente: {next_state}, Observación: {observation}")
        current_state = next_state
