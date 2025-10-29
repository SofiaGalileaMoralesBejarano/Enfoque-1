# Enfoque 1: Iteracion de politicas
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Este código implementa el algoritmo de iteración de políticas para un MDP, calculando la política óptima y la función de valor asociada.

# Inicio: 

class PolicyIteration:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states
        self.actions = actions
        self.transition_probabilities = transition_probabilities  # P(s'|s,a)
        self.rewards = rewards                                      # R(s,a,s')
        self.discount_factor = discount_factor                      # Factor de descuento gamma
        self.policy = {state: actions[0] for state in states}       # Política inicial arbitraria
        self.value_function = {state: 0 for state in states}        # Función de valor inicial

    def iterate(self, threshold):
        while True:
            self.policy_evaluation()            # Evalúa la política actual
            stable = self.policy_improvement()  # Mejora la política
            if stable:                          # Si no cambió ninguna acción, terminamos
                break

    def policy_evaluation(self):
        while True:
            delta = 0
            for state in self.states:
                v = self.value_function[state]
                action = self.policy[state]
                # Calcula el valor esperado de seguir la política en este estado
                self.value_function[state] = sum(
                    self.transition_probabilities[state][action][next_state] *
                    (self.rewards[state][action][next_state] +
                     self.discount_factor * self.value_function[next_state])
                    for next_state in self.states
                )
                delta = max(delta, abs(v - self.value_function[state]))
            if delta < 1e-6:  # Convergencia
                break

    def policy_improvement(self):
        stable = True
        for state in self.states:
            old_action = self.policy[state]
            # Selecciona la acción que maximiza el valor esperado
            self.policy[state] = max(self.actions, key=lambda action: self.calculate_action_value(state, action))
            if old_action != self.policy[state]:
                stable = False
        return stable

    def calculate_action_value(self, state, action):
        # Calcula el valor esperado de tomar una acción específica en un estado
        return sum(
            self.transition_probabilities[state][action][next_state] *
            (self.rewards[state][action][next_state] +
             self.discount_factor * self.value_function[next_state])
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

    pi = PolicyIteration(states, actions, transition_probabilities, rewards, discount_factor)
    pi.iterate(threshold=0.01)

    # Imprime la política final y la función de valor para cada estado
    print("Política final:", pi.policy)
    print("Función de valor final:", pi.value_function)
