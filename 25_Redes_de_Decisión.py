# Enfoque 1: Redes de decision
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Este código calcula el valor esperado de una red de decisiones, considerando decisiones discretas y sus posibles resultados con probabilidades.

# Inicio:

class Outcome:
    def __init__(self, utility, probability):
        self.utility = utility        # Valor de utilidad del resultado
        self.probability = probability  # Probabilidad de que ocurra el resultado

class DecisionNode:
    def __init__(self, decision, outcomes):
        self.decision = decision      # Valor asociado a la decisión
        self.outcomes = outcomes      # Lista de posibles resultados (Outcome)

class DecisionNetwork:
    def __init__(self):
        self.nodes = []               # Lista de nodos de decisión en la red

    def add_node(self, node):
        self.nodes.append(node)       # Agrega un nodo de decisión a la red

    def expected_value(self):
        # Calcula el valor esperado sumando para cada nodo:
        # decisión * suma de (utilidad * probabilidad) de cada resultado
        return sum(
            node.decision * sum(outcome.utility * outcome.probability for outcome in node.outcomes)
            for node in self.nodes
        )

# Definición de resultados para cada nodo
outcomes1 = [Outcome(10, 0.5), Outcome(20, 0.5)]  
outcomes2 = [Outcome(15, 0.3), Outcome(25, 0.7)]  

# Creación de nodos de decisión con sus resultados
node1 = DecisionNode(1, outcomes1)  
node2 = DecisionNode(2, outcomes2)  

# Construcción de la red de decisiones y adición de nodos
network = DecisionNetwork()
network.add_node(node1)
network.add_node(node2)

# Cálculo del valor esperado de la red
expected_value = network.expected_value()
print(f"El valor esperado de la red de decisiones es: {expected_value}")
