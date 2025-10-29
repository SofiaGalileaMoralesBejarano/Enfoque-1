# Enfoque 1: Exploración vs. Explotación
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Implementa un bandido multi-brazo con ε-greedy: en cada ronda, con probabilidad ε explora eligiendo un brazo al azar; con 1 explota el brazo con mejor promedio. 
# Actualiza incrementalmente las recompensas promedio por brazo y simula varias rondas para mostrar el balance exploración-explotación.


# Inicio de código:

import random

class EpsilonGreedyBandit:
    def __init__(self, arms, epsilon):
        self.arms = arms                # Lista de probabilidades de éxito de cada brazo
        self.epsilon = epsilon          # Probabilidad de exploración
        self.counts = [0] * len(arms)  # Veces que se ha elegido cada brazo
        self.values = [0.0] * len(arms) # Recompensa promedio de cada brazo

    def select_arm(self):
        # Elegir aleatoriamente (explorar) o elegir el mejor brazo (explotar)
        if random.random() < self.epsilon:
            return random.randint(0, len(self.arms) - 1)  # Explorar
        else:
            return self.values.index(max(self.values))    # Explotar

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        # Actualizar valor promedio incremental
        self.values[chosen_arm] = ((n - 1) / n) * value + (1 / n) * reward

    def simulate(self, rounds):
        total_reward = 0
        for _ in range(rounds):
            arm = self.select_arm()
            reward = 1 if random.random() < self.arms[arm] else 0
            self.update(arm, reward)
            total_reward += reward
        return total_reward

if __name__ == "__main__":
    # Probabilidades reales de éxito de cada brazo
    arms_probabilities = [0.2, 0.5, 0.75]
    epsilon = 0.1       # 10% de exploración
    rounds = 1000

    bandit = EpsilonGreedyBandit(arms_probabilities, epsilon)
    total_reward = bandit.simulate(rounds)

    print(f"Recompensa total tras {rounds} rondas: {total_reward}")
    print("Número de veces que se eligió cada brazo:", bandit.counts)
    print("Valor promedio estimado de cada brazo:", bandit.values)
