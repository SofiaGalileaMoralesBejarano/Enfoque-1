Enfoque 1: Propagacion de restricciones
# Autor: Sofia Galilea Morales Bejarano 6°E

# Este código resuelve un CSP mediante backtracking dirigido por conflictos, 
# retrocediendo directamente a la variable que causó el conflicto para evitar explorar ramas sin solución.

class ConflictDirectedBackjumping:
    def __init__(self, variables, domains, constraints):
        self.variables = variables                  # Lista de variables
        self.domains = domains                        # Diccionario de posibles valores
        self.constraints = constraints                # Función que valida restricciones
        self.solution = {}                            # Solución parcial o completa
        self.conflict_graph = {var: [] for var in variables}  # Registro de conflictos

    def is_valid(self, var, value):
        # Verifica si asignar 'value' a 'var' es válido con respecto a las variables ya asignadas
        for other in self.solution:
            if not self.constraints(var, value, other, self.solution[other]):
                self.conflict_graph[var].append(other)  # Registro de la variable en conflicto
                return False
        return True

    def backtrack(self):
        # Si todas las variables están asignadas, retorno la solución
        if len(self.solution) == len(self.variables):
            return self.solution

        var = self.select_unassigned_variable()  # Selecciono una variable sin asignar
        for value in self.domains[var]:
            if self.is_valid(var, value):
                self.solution[var] = value           # Asigno temporalmente
                result = self.backtrack()            # Continúo con recursión
                if result:
                    return result
                del self.solution[var]               # Retroceso si no hay solución

        # Si hay conflictos, realizo backjumping
        if var in self.conflict_graph and self.conflict_graph[var]:
            self.backjump(var)

        return None

    def backjump(self, var):
        # Elimino de la solución las variables que causaron conflicto
        for conflict in self.conflict_graph[var]:
            if conflict in self.solution:
                del self.solution[conflict]

    def select_unassigned_variable(self):
        # Retorna la primera variable sin asignar
        for var in self.variables:
            if var not in self.solution:
                return var
        return None

# Restricción: valores distintos
def constraints(var1, value1, var2, value2):
    return value1 != value2 

# Definición de variables y dominios
variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2],
    'B': [1, 2],
    'C': [1, 2]
}

# Creo el CSP con CDBJ y ejecuto el backtracking
csp = ConflictDirectedBackjumping(variables, domains, constraints)
solution = csp.backtrack()

# Imprimo la solución o indico que no existe
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
