# Enfoque 1: Acondicionamiento del corte
# Autor: Sofia Galilea Morales Bejarano 6°E

# Objetivo:
# Este código resuelve un CSP mediante backtracking combinado con cut conditioning: tras cada asignación, 
# reduce los dominios de las variables no asignadas según las restricciones, evitando conflictos y podando ramas inútiles.


# Inicio:

class CutConditioning:
    def __init__(self, variables, domains, constraints):
        self.variables = variables            # Lista de variables
        self.domains = domains                # Diccionario de posibles valores por variable
        self.constraints = constraints        # Función que valida restricciones
        self.solution = {}                    # Solución parcial o completa

    def is_valid(self, var, value):
        # Verifica si asignar 'value' a 'var' es válido con respecto a las variables ya asignadas
        for other in self.solution:
            if not self.constraints(var, value, other, self.solution[other]):
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
                self.apply_cut_conditioning(var)     # Aplico reducción de dominios a otras variables
                result = self.backtrack()            # Continúo recursivamente
                if result:
                    return result
                del self.solution[var]               # Retrocedo si no hay solución

        return None

    def apply_cut_conditioning(self, var):
        # Elimino de los dominios de las variables no asignadas los valores que causarían conflicto
        for other in self.variables:
            if other != var:
                self.domains[other] = [value for value in self.domains[other] if self.is_valid(other, value)]

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

# Creo el solver y ejecuto la búsqueda
cut_conditioning_solver = CutConditioning(variables, domains, constraints)
solution = cut_conditioning_solver.backtrack()

# Imprimo la solución o indico que no existe
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
