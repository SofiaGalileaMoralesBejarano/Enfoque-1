# Enfoque 1: MDP parcialmente observable POMDP
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Implementa un POMDP y calcula la función de valor mediante iteración de valores sobre estados de creencia, 
# incorporando la incertidumbre en las observaciones para obtener el valor/política óptimos.

# Inicio:

class POMDP:
    def __init__(self, states, actions, observations, transition_probabilities,
                 observation_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.observations = observations
        self.transition_probabilities = transition_probabilities  # P(s' | s, a)
        self.observation_probabilities = observation_probabilities  # P(o | s', a)
        self.rewards = rewards                                        # R(s, a, s')
        self.discount_factor = discount_factor                        # Factor de descuento gamma
        self.value_function = {state: 0 for state in states}         # Inicializa V(s) = 0

    def value_iteration(self, threshold):
        # Inicializa el estado de creencia uniforme
        belief_state = {state: 1 / len(self.states) for state in self.states}

        while True:
            delta = 0
            for state in self.states:
                v = self.value_function[state]
                # Actualiza V(s) con el máximo valor esperado sobre todas las acciones
                self.value_function[state] = max(
                    self.calculate_action_value(state, action, belief_state) for action in self.actions
                )
                delta = max(delta, abs(v - self.value_function[state]))
            if delta < threshold:  # Convergencia
                break

        return self.value_function

    def calculate_action_value(self, state, action, belief_state):
        # Calcula el valor esperado de tomar una acción dado un estado y estado de creencia
        expected_value = 0
        for next_state in self.states:
            for observation in self.observations:
                prob_transition = self.transition_probabilities[state][action][next_state]
                prob_observation = self.observation_probabilities[next_state][action][observation]
                reward = self.rewards[state][action][next_state]
                
                expected_value += (prob_transition * prob_observation *
                                   (reward + self.discount_factor *
                                    sum(belief_state[s] * self.value_function[s] for s in self.states)))
        return expected_value

if __name__ == "__main__":
    states = ['s1', 's2']
    actions = ['a1', 'a2']
    observations = ['o1', 'o2']

    # Probabilidades de transición P(s' | s, a)
    transition_probabilities = {
        's1': {'a1': {'s1': 0.7, 's2': 0.3}, 'a2': {'s1': 0.4, 's2': 0.6}},
        's2': {'a1': {'s1': 0.5, 's2': 0.5}, 'a2': {'s1': 0.2, 's2': 0.8}}
    }

    # Probabilidades de observación P(o | s', a)
    observation_probabilities = {
        's1': {'a1': {'o1': 0.9, 'o2': 0.1}, 'a2': {'o1': 0.6, 'o2': 0.4}},
        's2': {'a1': {'o1': 0.3, 'o2': 0.7}, 'a2': {'o1': 0.4, 'o2': 0.6}}
    }

    # Recompensas R(s, a, s')
    rewards = {
        's1': {'a1': {'s1': 10, 's2': 5}, 'a2': {'s1': 0, 's2': 1}},
        's2': {'a1': {'s1': 3, 's2': 7}, 'a2': {'s1': 1, 's2': 4}}
    }

    discount_factor = 0.9

    pomdp = POMDP(states, actions, observations,
                  transition_probabilities, observation_probabilities,
                  rewards, discount_factor)
    value_function = pomdp.value_iteration(threshold=0.01)

    print("Función de valor final:", value_function)
