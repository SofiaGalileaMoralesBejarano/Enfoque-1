Enfoque 1: Busqueda local minimos conflictos
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:

# Este código resuelve un CSP con búsqueda local: selecciona variables que están en conflicto y les asigna valores que reducen el número de conflictos, 
# intentando llegar a una asignación globalmente consistente.

# Inicio:

import random

class MinConflicts:
    def __init__(self, variables, domains, constraints, max_steps):
        self.variables = variables        # Lista de variables
        self.domains = domains            # Diccionario de posibles valores por variable
        self.constraints = constraints    # Función que valida restricciones
        self.max_steps = max_steps        # Máximo número de iteraciones

    def conflicts(self, assignment):
        # Cuenta el número de conflictos para cada variable
        conflict_count = {var: 0 for var in self.variables}
        for var in self.variables:
            for other in self.variables:
                if var != other and not self.constraints(var, assignment[var], other, assignment[other]):
                    conflict_count[var] += 1
        return conflict_count

    def solve(self):
        # Asignación inicial aleatoria
        assignment = {var: random.choice(self.domains[var]) for var in self.variables}

        for _ in range(self.max_steps):
            conflict_count = self.conflicts(assignment)
            # Si no hay conflictos, retornamos la solución
            if all(count == 0 for count in conflict_count.values()):
                return assignment

            # Selecciono variables que tienen conflictos
            conflicted_vars = [var for var, count in conflict_count.items() if count > 0]
            if not conflicted_vars:
                continue

            # Escogo una variable conflictiva y le asigno el valor que minimice conflictos
            var_to_change = random.choice(conflicted_vars)
            best_value = min(self.domains[var_to_change],
                             key=lambda value: self.evaluate_conflict(var_to_change, value, assignment))
            assignment[var_to_change] = best_value

        # Si no se encuentra solución dentro del límite de pasos, retorno None
        return None

    def evaluate_conflict(self, var, value, assignment):
        # Evalúa cuántos conflictos tendría la variable si se le asigna cierto valor
        temp_assignment = assignment.copy()
        temp_assignment[var] = value
        return self.conflicts(temp_assignment)[var]

# Restricción: valores distintos
def constraints(var1, value1, var2, value2):
    return value1 != value2

# Definición de variables y dominios
variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2],
    'B': [2, 3],
    'C': [1, 3]
}
max_steps = 100

# Creo el solver y ejecuto la búsqueda
min_conflicts_solver = MinConflicts(variables, domains, constraints, max_steps)
solution = min_conflicts_solver.solve()

# Imprimo la solución o indico que no existe
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
