# Enfoque 1: Búsqueda de la Política
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Este código calcula la política óptima de un MDP mediante iteración de política, 
# alternando entre evaluar los valores de los estados y mejorar la política hasta converger.



# Inicio:

class PolicySearch:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor):
        self.states = states  # Lista de estados del MDP
        self.actions = actions  # Lista de acciones posibles
        self.transition_probabilities = transition_probabilities  # P(s'|s,a)
        self.rewards = rewards  # R(s,a,s')
        self.discount_factor = discount_factor  # Factor de descuento γ
        self.policy = {state: actions[0] for state in states}  # Política inicial arbitraria
        self.value_function = {state: 0 for state in states}  # Inicializa valores de estados a 0

    def evaluate_policy(self):
        while True:
            delta = 0  # Diferencia máxima para medir convergencia
            for state in self.states:
                v = self.value_function[state]  # Valor actual del estado
                action = self.policy[state]  # Acción según la política actual
                # Calcula nuevo valor del estado como suma de probabilidades * (recompensa + valor descontado)
                self.value_function[state] = sum(
                    self.transition_probabilities[state][action][next_state] *
                    (self.rewards[state][action][next_state] + self.discount_factor * self.value_function[next_state])
                    for next_state in self.states
                )
                delta = max(delta, abs(v - self.value_function[state]))  # Actualiza delta
            if delta < 1e-6:  # Convergencia alcanzada
                break

    def improve_policy(self):
        stable = True  # Bandera para verificar si la política cambia
        for state in self.states:
            old_action = self.policy[state]  # Acción anterior
            # Selecciona la acción que maximiza el valor esperado
            best_action = max(self.actions, key=lambda action: sum(
                self.transition_probabilities[state][action][next_state] *
                (self.rewards[state][action][next_state] + self.discount_factor * self.value_function[next_state])
                for next_state in self.states
            ))
            self.policy[state] = best_action  # Actualiza la política
            if old_action != best_action:
                stable = False  # Si cambió alguna acción, la política no es estable
        return stable

    def find_policy(self):
        while True:
            self.evaluate_policy()  # Evalúa valores bajo la política actual
            if self.improve_policy():  # Mejora la política; termina si es estable
                break
        return self.policy, self.value_function  # Retorna política óptima y función de valor

# Ejemplo de uso
if __name__ == "__main__":
    states = ['s1', 's2']  # Estados del MDP
    actions = ['a1', 'a2']  # Acciones posibles

    # Probabilidades de transición P(s' | s, a)
    transition_probabilities = {
        's1': {'a1': {'s1': 0.8, 's2': 0.2}, 'a2': {'s1': 0.5, 's2': 0.5}},
        's2': {'a1': {'s1': 0.1, 's2': 0.9}, 'a2': {'s1': 0.3, 's2': 0.7}}
    }

    # Recompensas R(s, a, s')
    rewards = {
        's1': {'a1': {'s1': 5, 's2': 10}, 'a2': {'s1': 1, 's2': 2}},
        's2': {'a1': {'s1': 0, 's2': 3}, 'a2': {'s1': 4, 's2': 1}}
    }

    discount_factor = 0.9  # Factor de descuento

    # Crear instancia de búsqueda de política
    policy_search = PolicySearch(states, actions, transition_probabilities, rewards, discount_factor)
    policy, value_function = policy_search.find_policy()  # Ejecutar búsqueda

    # Imprimir resultados
    print("Política óptima:", policy)
    print("Función de valor final:", value_function)
