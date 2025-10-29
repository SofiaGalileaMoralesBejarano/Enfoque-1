Enfoque 1: Busqueda de vuelta atras
# Autor: Sofia Galilea Morales Bejarano 6°E


# Objetivo:
# Este código usa backtracking para generar todas las combinaciones posibles de k números tomados del rango 1 a n, 
# explorando recursivamente y retrocediendo cuando es necesario.

def backtrack(start, combination, n, k, results):
    # Si la combinación actual tiene k elementos, la agrego a los resultados
    if len(combination) == k:
        results.append(combination[:])  # Copio la lista para no modificarla luego
        return
    
    # Recorro los números posibles desde 'start' hasta 'n'
    for i in range(start, n + 1):
        combination.append(i)         # Agrego el número a la combinación actual
        backtrack(i + 1, combination, n, k, results)  # Llamada recursiva avanzando
        combination.pop()             # Retrocedo eliminando el último número agregado

def generate_combinations(n, k):
    results = []
    backtrack(1, [], n, k, results)  # Inicio la búsqueda desde 1 con combinación vacía
    return results

n = 5  # Límite superior de los números
k = 3  # Tamaño de cada combinación
combinations = generate_combinations(n, k)

# Imprimo todas las combinaciones encontradas
print("Combinaciones de", k, "números de 1 a", n, "son:")
for combo in combinations:
    print(combo)
