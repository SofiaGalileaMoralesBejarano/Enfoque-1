 Enfoque 1: Teoria juegos equilibrios mecanismos
# Autor: Sofia Galilea Morales Bejarano

# Objetivo: 

# Este código representa un juego de dos jugadores mediante matrices de pagos y busca equilibrios de Nash puros evaluando todas las combinaciones de estrategias posibles.


# Inicio: 

import itertools

class GameTheory:
    def __init__(self, strategies_p1, strategies_p2, payoff_matrix_p1, payoff_matrix_p2):
        self.strategies_p1 = strategies_p1
        self.strategies_p2 = strategies_p2
        self.payoff_matrix_p1 = payoff_matrix_p1
        self.payoff_matrix_p2 = payoff_matrix_p2

    def find_nash_equilibria(self):
        equilibria = []
        # Revisar todas las combinaciones de estrategias
        for s1, s2 in itertools.product(range(len(self.strategies_p1)), range(len(self.strategies_p2))):
            # Comprobar si P1 no puede mejorar su pago cambiando unilateralmente
            best_response_p1 = all(self.payoff_matrix_p1[s1][s2] >= self.payoff_matrix_p1[alt_s1][s2] for alt_s1 in range(len(self.strategies_p1)))
            # Comprobar si P2 no puede mejorar su pago cambiando unilateralmente
            best_response_p2 = all(self.payoff_matrix_p2[s1][s2] >= self.payoff_matrix_p2[s1][alt_s2] for alt_s2 in range(len(self.strategies_p2)))
            if best_response_p1 and best_response_p2:
                equilibria.append((self.strategies_p1[s1], self.strategies_p2[s2]))
        return equilibria

if __name__ == "__main__":
    # Estrategias de cada jugador
    strategies_p1 = ["Cooperar", "Traicionar"]
    strategies_p2 = ["Cooperar", "Traicionar"]

    # Matrices de pagos (fila: jugador 1, columna: jugador 2)
    payoff_matrix_p1 = [
        [3, 0],  # P1 coopera: P2 coopera=3, P2 traiciona=0
        [5, 1]   # P1 traiciona: P2 coopera=5, P2 traiciona=1
    ]
    payoff_matrix_p2 = [
        [3, 5],  # P1 coopera: P2 coopera=3, P2 traiciona=5
        [0, 1]   # P1 traiciona: P2 coopera=0, P2 traiciona=1
    ]

    game = GameTheory(strategies_p1, strategies_p2, payoff_matrix_p1, payoff_matrix_p2)
    nash_equilibria = game.find_nash_equilibria()

    if nash_equilibria:
        print("Equilibrios de Nash encontrados:")
        for eq in nash_equilibria:
            print(f"Jugador 1: {eq[0]}, Jugador 2: {eq[1]}")
    else:
        print("No se encontró equilibrio de Nash.")
